from math import inf # infinity for the initial value for the players
# ---------- My Samples for testing the algorithm:
from Node import Node
from my_samples import binary_tree, ternary_tree, tree_prune_example, tree_prune_slides_example


def minimax_prune(depth: int, node: Node, is_max_turn: bool, alpha=-inf, beta=inf):
    # Alpha is max value (initially -infinity)
    # Beta is min value (initially +infinity)
    if len(node.children) == 0: #then the node is terminal (leaf node)
        return node.value

    min_value = inf # initialize the min_value as +infinity
    max_value = -inf # initialize the max_value as -infinity
    value = None

    if is_max_turn == True:
        for child_node in node.children:
            value = minimax_prune(depth + 1, child_node, not is_max_turn, alpha, beta)
            max_value = max(max_value, value)
            alpha = max(alpha, value) # if `value` > alpha then update alpha
            if alpha >= beta:
                print(f"✂️  Do BETA PRUNING because alpha=({alpha}) and Beta=({beta})")
                break  #prune (no need to further explore this part of the tree)
        
        return max_value
    else:
        for child_node in node.children:
            value = minimax_prune(depth + 1, child_node, not is_max_turn, alpha, beta)
            min_value = min(min_value, value)
            beta = min(beta, value) # if `value` < beta then update beta
            if alpha >= beta:
                print(f"✂️  Do ALPHA PRUNING because alpha=({alpha}) and Beta=({beta})")
                break  #prune (no need to further explore this part of the tree)
        
        return min_value




# ====================== Testing the algorithm: ======================
# tree_prune_example.__str__()
# max_val = minimax_prune(depth=0, node=tree_prune_example, is_max_turn=True)
# print(f"max_value: {max_val}")

# # --- Now let's play to get the MIN value: (start playing as the MIN player)
# min_val = minimax_prune(depth=0, node=tree_prune_example, is_max_turn=False)
# print(f"min_value: {min_val}")

# ====================== Example from Slides: ======================
tree_prune_slides_example.__str__()
max_val = minimax_prune(depth=0, node=tree_prune_slides_example, is_max_turn=True)
print(f"max_value: {max_val}")


# # --- Now let's play to get the MIN value: (start playing as the MIN player)
# min_val = minimax_prune(depth=0, node=tree_prune_slides_example, is_max_turn=False)
# print(f"min_value: {min_val}")