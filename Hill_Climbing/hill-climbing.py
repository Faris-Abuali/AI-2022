import random
# We need to randomize a lot of things 

class Space:
    def __init__(self, height, width, num_hospitals):
        self.height = height
        self.width = width
        self.num_hospitals = num_hospitals
        self.houses = set() # set of tuples
        self.hospitals = set() # set of tuples

    def add_house(self, row, col): 
        # to add house on the problem space
        self.houses.add((row, col)) # add a new tuple to the houses set

    def available_space(self):
        # To find the available location to place the houses and the hospitals
        candidates = set(
            (row, col)
            for row in range(self.height)
            for col in range(self.width)
        )
        # Now `candidates` is a set of tuples of all possible coordinates in our space
        # Let's remove the un-vacant tuples from the `candidates` set:
        for house in self.houses:
            candidates.remove(house)
        for hospital in self.hospitals:
            candidates.remove(hospital)
        return candidates

    def get_cost(self, hospitals):
        # The cost is the sum of all distances between each house and its nearest hospital:
        cost = 0
        for house in self.houses:
            # Find the Manhattan distance (cost) between the current house and its nearest hospital
            # Manhattan distance: (house_row - hospital_row) + (house_col - hospital_col)
            cost += min(
                abs(house[0] - hospital[0]) + abs(house[1] - hospital[1])
                for hospital in hospitals
            )

        #  --- The above code is a shorthand for the below: ----
        # for house in self.houses:
        #     distancesFromCurrentHouseToHospitals = [] # clear the list
        #     for hospital in hospitals:
        #         c = abs(house[0] - hospital[0]) + abs(house[1] - hospital[1])
        #         distancesFromCurrentHouseToHospitals.append(c)
        #     cost += min(distancesFromCurrentHouseToHospitals)
        return cost

    def get_neighbors(self, row, col):
        # To find out the valid neighbors
        candidates = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]
        neighbors = []
        # But it may be the case that not all candidates are available neighbors:
        for (r, c) in candidates:
            if (r, c) in self.houses or (r, c) in self.hospitals:
                continue # then this spot is reserved by a house or a hospital
            if  0 <= r < self.height and 0 <= c < self.width:
                neighbors.append((r, c)) # Then this tuple (r, c) is an available neighbor
        return neighbors

    def output_image(self, filename):
        # This method is not part of the optimization, but we want to show the output graphically
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        cost_size = 40
        padding = 10

        img = Image.new("RGBA",
                        (self.width * cell_size, self.height * cell_size + cost_size + padding * 2),
                        "white"
                        )
        houseImg = Image.open("./assets/images/House.png").resize((cell_size, cell_size))
        hospitalImg = Image.open("./assets/images/Hospital.png").resize((cell_size, cell_size))
        font = ImageFont.truetype("./assets/fonts/OpenSans-Regular.ttf", 30)
        draw = ImageDraw.Draw(img)

        for row in range(self.height):
            for col in range(self.width):
                rect = [
                    (col * cell_size + cell_border, row * cell_size + cell_border),
                    ((col + 1) * cell_size - cell_border, (row + 1) * cell_size - cell_border)
                ]
                draw.rectangle(rect, fill="black")

                if (row, col) in self.houses:
                    img.paste(houseImg, rect[0], houseImg)
                if (row, col) in self.hospitals:
                    img.paste(hospitalImg, rect[0], hospitalImg)

        draw.rectangle(
            (0, self.height * cell_size, self.width * cell_size, self.height * cell_size + cost_size + padding * 2),
            "black"
        )

        draw.text(
            (padding, self.height * cell_size + padding),
            f"Cost: {self.get_cost(self.hospitals)}",
            fill="white",
            font=font
        )

        img.save(f"./output/{filename}")

    def hill_climb(self, maximum=None, image_prefix=None, log=False):
        count = 0 # counter to exit the while loop when number of iterations exceeds the maximum (if there is a maximum parameter number specified)

        # We want to add hospitals randomly to the grid:
        self.hospitals = set() # clear the set of hospitals first in case of previous function calls were made.
        # Now, add hospitals randomly to the grid:
        for i in range(self.num_hospitals):
            self.hospitals.add(random.choice(list(self.available_space())))
            # 1. self.available_space() returns a SET of all available spaces.
            # 2. convert the set to list, and chose one tuple randomly, this chosen tuple will be the coordinates (row, col) of the newly added house. 
        if log:
            print("Initial state: Cost", self.get_cost(self.hospitals))
        if image_prefix:
            self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")

        # If there's no maximum parameter specified, the while loop will run until we reach a state where the cost can no more be optimized:
        while maximum is None or count < maximum:
            count += 1
            best_neighbors = [] # list of sets???
            best_neighbor_cost = None

            for hospital in self.hospitals:
                # `hospital` is a tuple: (row, col)
                for replacement in self.get_neighbors(*hospital): 
                    # *hospital means pass all the tuple 
                    # similar to: self.get_neighbors(hospital[0], hospital[1])
                    hospitals_new_coordinates = self.hospitals.copy() # make a copy of the current set of coordinates
                    hospitals_new_coordinates.remove(hospital) # we ask ourselves, what would happen if we moved this hospital to its new neighbor place:
                    hospitals_new_coordinates.add(replacement)
                    # Will the cost of the new coordinates increase? decrease? or stay the same? 👇
                    cost = self.get_cost(hospitals_new_coordinates)
                    if best_neighbor_cost is None or cost < best_neighbor_cost:
                        best_neighbor_cost = cost
                        best_neighbors = [hospitals_new_coordinates] # convert the set `hospitals_new_coordinates` to list.
                    elif best_neighbor_cost == cost:
                        # In case when more than one neighbor had the same cost, don't overwrite the set of `hospitals_new_coordinates`, instead, save them all in a list and then one of them will be chosen randomly.
                        best_neighbors.append(hospitals_new_coordinates)

            if self.get_cost(self.hospitals) < best_neighbor_cost:
                # then the current state (current hospitals places) still give the best (least) cost. In the above 2 for loops, we tried to move all hospitals to their neighbor places, but nothing of the new movements gave us a better cost than the current state's cost, so now there is nothing we can do to optimize more. We should quit:
                return self.hospitals # return the coordinates of the hospitals (set of tuples)

            else:
                if log:
                    print(f"Found Better Neighbor: cost {best_neighbor_cost}")
                self.hospitals = random.choice(best_neighbors)

            if image_prefix:
                self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")
# ------------------------- End `Space` Class ---------------------------

s = Space(height=6, width=12, num_hospitals=3) 
# Add 5 houses to the grid randomly:
for i in range(5):
    s.add_house(random.randrange(s.height), random.randrange(s.width)) # add_house(row, col)

hospitals = s.hill_climb(30, image_prefix="hospitals", log=True)
# Maximum Iterations = 30
