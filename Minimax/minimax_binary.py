import math, random
from math import inf # infinity for the initial value for the players

def mini_max(current_depth, index, maxTurn, scores, total_depth):
    if current_depth == total_depth:
        return scores[index]
    
    if maxTurn == True:
        return max(
            mini_max(current_depth + 1, index*2, not maxTurn, scores, total_depth),
            mini_max(current_depth + 1, index*2+1, not maxTurn, scores, total_depth)
        )
    else: #then it is the MIN player's turn
        return min(
            mini_max(current_depth + 1, index*2, not maxTurn, scores, total_depth),
            mini_max(current_depth + 1, index*2+1, not maxTurn, scores, total_depth)
        )
# ------------------- End mini_max method -----------------------


# ------ Note: The above function works for a binary tree only. --------
# see this image that I used as an example: https://i.imgur.com/J7OBNra.png


terminalNodes = [50, 70, 60, 90, 10, 50, 60, 70, 80, 90, 20, 30, 40, 23, 40, 30] # terminal nodes means leaf nodes
numberOfLeaves = len(terminalNodes) 
total_depth = math.log(numberOfLeaves, 2) # example: If leaf nodes = 16, then log(16, 2) = 4 (so, depth is 4)
current_depth = 0  # start from the root of the tree (So, current_depth = 0)
nodeValue = 0
maxTurn = True

print("The answer is: ", end=" ")
answer = mini_max(current_depth, nodeValue, maxTurn, terminalNodes, total_depth)
print(answer)