# ------------------- Global Variables ----------------------
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8, 9],
    5: [10, 11],
    6: [12, 13],
    7: [14, 15],
    8: [16],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
};
expanded = []
# --------------------------------------------------------------------

def dls(node, limit):
    if limit >= 0:
        expanded.append(node)
        for child in graph[node]:
            if child not in expanded:
                dls(child, limit-1)

# ---------------------------------------------
def dls_with_goal(node, limit, goal):
    if limit >= 0:
        expanded.append(node)
        if node == goal:
            return True
        for child in graph[node]:
            if child not in expanded:
                f = dls_with_goal(child, limit-1, goal)
                if f == True:
                    return True
# ---------------------------------------------



# ---------------------------------------------------
expanded = []
print("----- DLS ------")
dls(2)
print(expanded)
# ------------------------------------------
