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
}

def bfs(graph, start, goal): 
    stack, temp, expanded = [], [], []
    stack.append([start]) # as a list
    while stack: # while stack not empty
        top = stack.pop(0) # as a `Queue`, pop the first element, this is a list (the whole path)
        vertex = top[-1] # take the last node of the `top`
        expanded.append(vertex) # the closed set
        if goal == vertex: 
            print("expanded: ", expanded) 
            print("solution: ", top) # top is the list that represents the path (the solution)
            return
        for child in graph[vertex]:
            newList = list(top)
            newList.append(child)
            stack.append(newList)
        # now reverse the temp stack
        while temp:
            stack.append(temp.pop())
    else: 
        print("expanded: ", expanded) 
        print("Goal not found")

bfs(graph, 1, 6)
