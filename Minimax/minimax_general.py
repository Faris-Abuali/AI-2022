from math import inf # infinity for the initial value for the players
# ---------- My Samples for testing the algorithm:
from Node import Node # My `Node` class
from my_samples import binary_tree, ternary_tree


def mini_max(depth: int, node: Node, is_max_turn: bool):
    if len(node.children) == 0: #then the node is terminal (leaf node)
        return node.value

    min_value = inf # initialize the min_value as +infinity
    max_value = -inf # initialize the max_value as -infinity
    value = None

    if is_max_turn == True:
        for child_node in node.children:
            value = mini_max(depth + 1, child_node, not is_max_turn)
            max_value = max(max_value, value)
        
        return max_value
    else: 
        # then it is player MIN's turn
        for child_node in node.children:
            value = mini_max(depth + 1, child_node, not is_max_turn)
            min_value = min(min_value, value)

        return min_value

# ---------------------------------------------------------------

# ====================== Testing the algorithm: ======================
binary_tree.__str__()
max_val = mini_max(depth=0, node=binary_tree, is_max_turn=True)
print(f"max_value: {max_val}")

# --- Now let's play to get the MIN value: (start playing as the MIN player)
min_val = mini_max(depth=0, node=binary_tree, is_max_turn=False)
print(f"min_value: {min_val}")


# -------------- Non-binary Tree (Ternary or any other type) ---------------
ternary_tree.__str__()
max_val = mini_max(depth=0, node=ternary_tree, is_max_turn=True)
print(f"max_value: {max_val}")

# --- Now let's play to get the MIN value: (start playing as the MIN player)
min_val = mini_max(depth=0, node=ternary_tree, is_max_turn=False)
print(f"min_value: {min_val}")
