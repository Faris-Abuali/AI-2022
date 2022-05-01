import imp
from sys import maxsize  # a big number to represent infinity


INFINITY = maxsize
# Tree Builders
class Node(object):
    def __init__(self,depth, player_turn, sticks_remaining, value=0):
        self.depth = depth # How deep we are into the tree
        self.player_turn = player_turn # Either +1 or -1
        self.sticks_remaining = sticks_remaining 
        self.value = value # The game state (the value that each node holds) 
        # either infinity, 0, or -infinity
        self.children = []
        self.create_children() # invoke a class function

    def __str__(self):
        print("-----------------------------------------------------------")
        print(f"depth: {self.depth}")
        print(f"player_turn: {self.player_turn}")
        print(f"sticks_remaining: {self.sticks_remaining}")
        print(f"value: {self.value}")
        print(f"children: ")
        for child in self.children:
            print("\t #### Child: #####")
            print(f"\tdepth: {child.depth}")
            print(f"\tplayer_turn: {child.player_turn}")
            print(f"\tsticks_remaining: {child.sticks_remaining}")
            print(f"\tvalue: {child.value}")
        print("-----------------------------------------------------------")


    def create_children(self):
        if self.depth >= 0:
            new_depth = self.depth - 1
            new_player_turn = - self.player_turn  # toggle the turn (multiply by -1)
            for i in range(1, 3):  # each node will have 2 children (binary)
                new_remaining_sticks = self.sticks_remaining - i
                new_value = self.real_val(new_remaining_sticks)
                self.children.append(
                    Node(new_depth, new_player_turn, new_remaining_sticks, new_value)
                )

    def real_val(self, sticks_remaining):
        if sticks_remaining == 0:  # then the node is terminal node
            return INFINITY * self.player_turn
        elif sticks_remaining < 0:
            return INFINITY * (- self.player_turn)
        return 0
# ------------------------------ End `Node` Class ------------------------------
## Algorithm:
def min_max(node, depth, player_turn):
    if depth == 0 or abs(node.value) == INFINITY:
        return node.value
    
    best_value = INFINITY * (- player_turn)

    for i in range(len(node.children)):
        child = node.children[i]
        value = min_max(child, depth - 1, -player_turn)
        child_value = abs(INFINITY * player_turn - value)
        parent_value = abs(INFINITY * player_turn - best_value)
        if child_value < parent_value:
            best_value = child_value

    return best_value

## IMPLEMENTATION
def win_check(num_sticks, player_turn):
    if num_sticks <= 0:
        print ("*"*30)
        if player_turn > 0:
            if num_sticks == 0:
                print ("\tYou WIN!!!")
            else:
                print ("\tTOO MANY! You lose...")
        else:
            if num_sticks == 0:
                print ("\tComp Wins... Better luck next time.")
            else:
                print ("\tCOMP ERROR!")

        print ("*"*30)
        return True # True means the game is over
    return False # False means the game still not over

# ----------------------- Test Drive ------------------------------------
if __name__ == "__main__":
    total_sticks = 11
    depth = 4
    player_turn = 1 # 1 means you, -1 means computer
    print("INSTRUCTIONS: The player who picks up the last stick is the winner")
    print("You can only pick up either one (1) or two (2) sticks at a time:")

    while total_sticks > 0:
        print(f"{total_sticks} remain. How many sticks do you want to pick?")
        num_picked_sticks = int(input("1 or 2?: "))
        total_sticks -= num_picked_sticks
        is_game_over = win_check(total_sticks, player_turn)
        if not is_game_over:
            player_turn *= -1 # toggle the player's turn
            node = Node(depth, player_turn, total_sticks)
            node.__str__()
            best_choice = -100 # this variable will decide either 1 or 2 sticks will be the best choice for the computer
            best_value = INFINITY * (-player_turn)
            for i in range(len(node.children)):
                child = node.children[i]
                val = min_max(child, depth, -player_turn)
                child_value = abs(INFINITY * player_turn - val)
                parent_value = abs(INFINITY * player_turn - best_value)
                if child_value <= parent_value:
                    best_value = val
                    best_choice = i
            best_choice += 1
            print(f"Computer chose: {str(best_choice)}, based on value: {str(best_value)}")
            total_sticks -= best_choice
            is_game_over = win_check(total_sticks, player_turn)
            player_turn *= -1 # toggle the player's turn

