from collections import defaultdict
# defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
import json


class Graph:
    def __init__(self):
        self.graphlist = {}  # dictionary of key=source, value=list of all successors
        self.expanded_nodes = []
        self.__str__()

    def __init__(self, initial_graph):
        self.graphlist = initial_graph
        self.expanded_nodes = []
        self.__str__()

    def __str__(self):
        print("------- Graphlist: -------")
        # 1. Print a dictionary line by line by iterating over keys
        for (key, value) in self.graphlist.items():
            # .items() returns a list of tuples, each tuple is (key, value)
            print(f"{key}: {value}")
        # -------------------------------------------------------
        # 2. Print a dictionary line by line using json.dumps()
        # print(json.dumps(self.graphlist, indent=4))
        print("--------------------------")

    def add_edge(self, source, destination):
        # graphlist is a dictionary, each key is the source node, and its value is a list of all successor nodes (neighbor nodes)
        if source in self.graphlist:
            # the source exists, just append the new destination to the source's list
            self.graphlist[source].append(destination)
        else:
            # add the new source to the dictionary
            self.graphlist.update({source: [destination]}) 

    def get_expanded_nodes(self):
        return self.expanded_nodes

    def dfs_rec(self, current_node, goal_node, visited_nodes):
        visited_nodes.append(current_node)  # add the node to the list of visited nodes ✅
        # print(current_node, end=" ")
        self.expanded_nodes.append(current_node)

        # Check if we have reached the goal node:
        if current_node == goal_node:
            return True  # True means the goal is found, no need to explore further ✅

        for successor in self.graphlist[current_node]:
            if successor not in visited_nodes:
                found = self.dfs_rec(successor, goal_node, visited_nodes)
                if found: return True
        
        return False # False means the goal is not found (yet) ❌

    def dfs(self, start_node, goal_node):
        visited_nodes = [] #list of all visited nodes (initially empty)
        found = self.dfs_rec(start_node, goal_node, visited_nodes)
        print()
        feedback = f"Goal: {goal_node} was found ✅" if found else f"Goal: {goal_node} wasn't found ❌"
        print(feedback)

# -------------------------- Receive inputs from user ----------------------------------------
# g = Graph()
# edges_count = int(input("Enter total edges: "))
# for i in range(edges_count):
#     source=int(input("source: "))
#     dest=int(input("dest.: "))
#     g.add_edge(source, dest)

# g.__str__()

# # s =int(input("Enter a starting node: "))
# # g.dfs(s)
# ------------------------------------------------------------------------------------------


# graph = {
#     1: [2, 3],
#     2: [4, 5],
#     3: [6, 7],
#     4: [8, 9],
#     5: [10, 11],
#     6: [12, 13],
#     7: [14, 15],
#     8: [16],
#     9: [],
#     10: [],
#     11: [],
#     12: [],
#     13: [],
#     14: [],
#     15: [],
#     16: [],
# }

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],
    "H": ["P"],
    "I": [],
    "J": [],
    "K": [],
    "L": [],
    "M": [],
    "N": [],
    "O": [],
    "P": [],
}

g = Graph(graph)
g.dfs("A", "K")
print(g.get_expanded_nodes())
