from operator import truediv
import pygame
import math
from queue import PriorityQueue
import time

ROWS = 25 
WIDTH = 600
# the (width, height) dimensions of the window
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Algorithm")

RED = (255, 0, 0)  # node is in the closed set
GREEN = (0, 255, 0)  # node is in the open list
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)  # un-explored yet
BLACK = (0, 0, 0)  # a barrier (obstacle)
PURPLE = (128, 0, 128)  # the path
ORANGE = (255, 165, 0)  # the start node
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return (self.row, self.col)

    def is_start(self):
        return self.color == ORANGE

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE
    # --------------------------------------------------

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE
    # --------------------------------------------------

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
        # remember: height = width here (we are drawing a square instead of rectangle)

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
# ------------------------------ End Class Spot ------------------------------

# heuristic function h(n)
def h(point1, point2):
    x1, y1 = point1  # destructure the point1 coordinates
    x2, y2 = point2  # destructure the point2 coordinates
    return abs(y1 - y2) + abs(x1 - x2)  # Manhattan Distance

def reconstruct_path(came_from, current, draw):
    print("---- Path from Start to Goal 🛤️: ------")
    while current in came_from:
        print(current.get_pos())
        current = came_from[current]
        current.make_path()
        draw()

def algorithm(draw, grid, start, end):
    # draw: is a function passed as an argument
    # remember when we call this `algorithm` function, we do like this: 👇
    # algorithm(lambda: draw(window, grid, ROWS, width), grid, start, end)
    # We passed anonymous function to be able to use the draw function here. 
    # Now we can use the draw function without passing any parameters: draw()✅ not draw(window, grid, ROWS, width)❌ because when we say draw() we are actually calling the anonymous function which in turn, invokes the draw(window, grid, ROWS, width):
    # draw: lambda: draw(window, grid, ROWS, width)

    # start: the start node (object of Spot class) 
    # end: the end node (object of Spot class) 

    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start)) # a tuple of: (priority, timestamp, spot (the node itself))
    # I am using the count as a timestamp to indicate when this node was added to the queue.
    # We resort to this timestamp as a tie breaker when we face multiple nodes that have the same priority, so we decide to pull the node which entered the queue first.
    came_from = {}
    # Dictionary to store all g_scores (costs) for all spots:
    g_score = {spot: float("inf") for row in grid for spot in row} # key= the spot object itself, and value= infinity for now
    # The above line is equivalent to:
    # for row in grid:
    #     for spot in row:
    #         g_score[spot] = float("inf")
    g_score[start] = 0 # Since g_score means "the distance(cost) from start node to the current node", it is sensible to say that g(start) = 0 
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos()) 
    #f(start) = g(start) + h(start) = 0 + h(start) = h(start)

    # The priorityQueue doesn't tell us if a node exists in it or not, so we make a set called open_set_hash to keep track of the nodes which are currently in the priorityQueue:
    open_set_hash = {start} 

    while not open_set.empty():
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()

        current = open_set.get()[2] #remember: each entry in the open_set is a tuple: (priority, timestamp, spot)
        # ---- Remove the lowest-cost node from the open_set (priorityQueue): --------
        open_set_hash.remove(current)

        if current == end: 
            # then congrats! we have reached the goal node (the `end` spot)
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True #Stop the algorithm 

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1 # Each edge's cost = 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    # then add the neighbor to the open_set (to the priorityQueue)
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor)) # (priority, timestamp, node)
                    open_set_hash.add(neighbor)
                    neighbor.make_open() # to indicate that this node (spot) has become explored

        # After recognizing all the current node's neighbors, invoke the draw to update the UI:
        draw() # the neighbors (successors) of `current` node will now appear in GREEN

        if current != start:
            current.make_closed() # shouldn't we add the current node to a `closed_set`???
        
        time.sleep(0.1) # delay for 1 second

    return False
    

def make_grid(rows, width):
    # Our square grid will be something like this: 
    # - List of lists, each list represents a row in the grid.
    # - Each row stores a number of spots.
    # [
    #     [spot, spot, spot, ..., spot],
    #     [spot, spot, spot, ..., spot],
    #     [spot, spot, spot, ..., spot],
    #     [spot, spot, spot, ..., spot],
    #     ...
    #     [spot, spot, spot, ..., spot],
    # ]

    grid: list[list[Spot]] = []    
    gap = width // rows
    # width: The width of our entire grid (ex: 800px)
    # rows: How many rows we have (ex: 50)
    # gap: indicates what the width of each spot (node) should be (ex: 800px/50 = 16px)
    for i in range(rows):
        grid.append([])  # append new list (row) to the grid
        for j in range(rows):
            spot = Spot(i, j, gap, rows)  # (row, col, width, total_rows)
            grid[i].append(spot) # append a new spot (node) to the current row (grid[i])
    return grid


def draw_grid(window, rows, width):
    gap = width // rows
    # width: The width of our entire grid (ex: 800px)
    # rows: How many rows we have (ex: 50)
    # gap: indicates what the width of each spot (node) should be (ex: 800px/50 = 16px)
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
        # ☝️ draws a horizontal line from (x=0, y=i*gap) --> (x=width, y=i*gap)
    for i in range(rows):
        pygame.draw.line(window, GREY, (i * gap, 0), (i * gap, width))
        # ☝️ draws a vertical line from (x=i*gap, y=0) --> (x=i*gap, y=width)

def draw(window, grid: "list[list[Spot]]", rows, width):
    window.fill(WHITE) #fills the entire screen with one color, you do this at the beginning of every frame

    # 1. Draw all the spots (nodes)
    for row in grid:
        for spot in row:
            spot.draw(window) #call the method (draw) of the Spot class and pass the window obj
            
    # 2. Next, we will draw the grid's lines (borders):
    draw_grid(window, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    # pos: the mouse position
    gap = width // rows
    # width: The width of our entire grid (ex: 800px)
    # rows: How many rows we have (ex: 50)
    # gap: indicates what the width of each spot (node) should be (ex: 800px/50 = 16px)
    (y, x) = pos # the `pos` tuple is known from the pygame's built-in function (get_pos) 

    row = y // gap
    col = x // gap
    # print(f"row: {row}, col: {col}")

    return (row, col) # return the row and col of the spot (node) on which the user has clicked

def main(window, width):
    # width: the windows' width (ex: 800px)
    grid: list[list[Spot]] = make_grid(ROWS, width)

    # to keep track of the `start` and `end` Spots:
    start: Spot = None
    end: Spot = None

    run = True #indicates wether we are running the main loop or not
    started = False #indicates wether we started the algorithm or not

    while run:
        draw(window, grid, ROWS, width) #this will internally invoke the `draw_grid` function
        for event in pygame.event.get(): #returns list of events (List[Event])
            if event.type == pygame.QUIT:
                run = False #stop the game

            if started:
                continue #Once the algorithm starts searching on finding the path, prevent the user from changing anything such as changing the barriers(obstacles) and so on..
            
            if pygame.mouse.get_pressed()[0]: # MOUSE'S LEFT BUTTON CLICKED
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width) # gives us the row, col indexes of the node (spot) on which the user clicked
                spot = grid[row][col] #Now I grab the spot (node) on which the user clicked.
                # -----------------------------------------------------------------
                # --- The first click will set the clicked spot (node) as the start spot ---
                if not start and spot != end:
                    start = spot
                    start.make_start()
                # --- The second click will set the clicked spot (node) as the end spot ---
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                # --- Now after the `start` and `end` spots are specified, each click on a spot will make this spot a barrier (obstacle) ---
                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # MOUSE'S RIGHT BUTTON CLICKED
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset() #call the `reset` method which we defined in Spot class
                if spot == start:
                    start = None # clear the spot
                elif spot == end: 
                    end = None # clear the spot

            # ---- After Specifing the `start` and `end` spots, and placing the barriers (obstacles), now we are ready to press the SPACE key to trigger the algorithm:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid) #Let each spot recognize its neighbors (successors (all possible moves))

                    algorithm(lambda: draw(window, grid, ROWS, width), grid, start, end)
                    
    
    # pygame.quit() # quits the pygame window

main(WINDOW, WIDTH)

