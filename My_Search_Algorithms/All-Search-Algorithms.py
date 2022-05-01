from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
from collections import defaultdict
from ssl import SSLSocket
from samples import graph, graph_weighted, weighted_graph_from_slides  # My graph samples
from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.graphlist = {}  # dictionary of key=source, value=list of all successors
        self.expanded_nodes = []
        self.predecessors = {}
        self.__str__()

    def __init__(self, initial_graph):
        self.graphlist = initial_graph
        self.expanded_nodes = []
        self.predecessors = {}
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

    def add_edge(self, source, destination, directed=True):
        # graphlist is a dictionary, each key is the source node, and its value is a list of all successor nodes (neighbor nodes)
        if source in self.graphlist:
            # the source exists, just append the new destination to the source's list
            self.graphlist[source].append(destination)
        else:
            # add the new source to the dictionary
            self.graphlist.update({source: [destination]})

        if not directed:
            # then add another edge:
            if destination in self.graphlist:
                # the source exists, just append the new destination to the source's list
                self.graphlist[destination].append(source)
            else:
                # add the new source to the dictionary
                self.graphlist.update({destination: [source]})

    def add_edge(self, source, destination, weight, directed=True):
        # Add edges between two nodes along with weight, this is needed for algorithms such as Unifrom Cost Search:

        # graphlist is a dictionary, each key is the source node, and its value is a list of all successor nodes (neighbor nodes)
        # The value will be a tuple: (weight, data)
        value = (weight, destination)
        if source in self.graphlist:
            # the source exists, just append the new destination to the source's list
            self.graphlist[source].append(value)
        else:
            # add the new source to the dictionary
            self.graphlist.update({source: [value]})

        if not directed:
            # then add another edge:
            # The value will be a tuple: (weight, data)
            value = (weight, source)
            if destination in self.graphlist:
                # the source exists, just append the new destination to the source's list
                self.graphlist[destination].append(value)
            else:
                # add the new source to the dictionary
                self.graphlist.update({destination: [value]})

    def get_expanded_nodes(self):
        return self.expanded_nodes

    def get_path(self, current_node):
        path = [current_node]  # ["J"]
        while current_node in self.predecessors:
            current_node = self.predecessors[current_node]
            path.insert(0, current_node)  # ["A", "B", "E", "J"]
        return path

    def clear_expanded_nodes_and_predecessors(self):
        self.expanded_nodes.clear()
        self.predecessors.clear()

# --- DFS --- DFS --- DFS --- DFS --- DFS --- DFS --- DFS --- DFS --- DFS --- DFS --- DFS ---
    def dfs_rec(self, current_node, goal_node, visited_nodes):
        # add the node to the list of visited nodes ✅
        visited_nodes.append(current_node)
        # print(current_node, end=" ")
        self.expanded_nodes.append(current_node)

        # Check if we have reached the goal node:
        if current_node == goal_node:
            return True  # True means the goal is found, no need to explore further ✅

        for successor in self.graphlist[current_node]:
            if successor not in visited_nodes:
                self.predecessors[successor] = current_node
                found = self.dfs_rec(successor, goal_node, visited_nodes)
                if found:
                    return True

        return False  # False means the goal is not found (yet) ❌

    def dfs(self, start_node, goal_node):
        visited_nodes = []  # list of all visited nodes (initially empty)
        found = self.dfs_rec(start_node, goal_node, visited_nodes)
        # feedback = f"Goal: {goal_node} was found ✅" if found else f"Goal: {goal_node} wasn't found ❌"
        # print(feedback)

# --- DLS --- DLS --- DLS --- DLS --- DLS --- DLS--- DLS --- DLS --- DLS --- DLS --- DLS ---
    def dls_rec(self, current_node, goal_node, visited_nodes, limit):
        if limit <= 0:
            # stop expanding this node because it's in a level that exceeds the limit.
            return False
        # add the node to the list of visited nodes ✅
        visited_nodes.append(current_node)
        # print(current_node, end=" ")
        self.expanded_nodes.append(current_node)

        # Check if we have reached the goal node:
        if current_node == goal_node:
            return True  # True means the goal is found, no need to explore further ✅

        for successor in self.graphlist[current_node]:
            if successor not in visited_nodes:
                self.predecessors[successor] = current_node
                found = self.dls_rec(successor, goal_node, visited_nodes, limit-1)
                if found:
                    return True

        return False  # False means the goal is not found (yet) ❌

    def dls(self, start_node, goal_node, limit):
        visited_nodes = []  # list of all visited nodes (initially empty)
        found = self.dls_rec(start_node, goal_node, visited_nodes, limit)
        print()
        feedback = f"Goal: {goal_node} was found ✅" if found else f"Goal: {goal_node} wasn't found ❌"
        print(feedback)
        return found

# --- IDS --- IDS --- IDS --- IDS --- IDS --- IDS --- IDS --- IDS --- IDS --- IDS --- IDS ---
# --- After implementing the DLS, we can implement the Iterative Deepening Search algorithm, making use of the same dls() function we used to implement the DLS (Depth-Limited Search): ---
    def iterative_deepining_search(self, start_node, goal_node, stop, step):
        found = False
        for i in range(0, stop, step):
            found = self.dls(start_node, goal_node, i)
            print(self.get_expanded_nodes())
            self.clear_expanded_nodes()
            if found:
                break
        return found

# --- BFS --- BFS --- BFS --- BFS --- BFS --- BFS --- BFS --- BFS --- BFS --- BFS --- BFS ---
    def bfs(self, start_node, goal_node):
        visited_nodes = []  # list of all visited nodes (initially empty)
        # Initialize empty queue:
        queue = []

        # visited_nodes.append(start_node) # Add the start node to the `visited_nodes` list
        queue.insert(0, start_node)  # Enqueue the start_node to the queue:
        while queue:
            # dequeue the first node from the queue (FIFO)
            current_node = queue.pop(0)
            visited_nodes.append(current_node)
            self.expanded_nodes.append(current_node)

            # Check if we reached the goal_node:
            if current_node == goal_node:
                return True  # True means we reached the goal ✅

            # Check neighbors(successors) for the current_node:
            for successor in self.graphlist[current_node]:
                if successor not in visited_nodes:
                    queue.append(successor)
                    self.predecessors[successor] = current_node

        return False  # False means the goal was NOT reached ❌

    def reconstruct_ucs_path(self, current_node, path=[]):   
        if current_node is not None:
            # path.insert(0, current_node)
            for (weight, node, predecessor) in self.expanded_nodes:
                if node == current_node:
                    path.insert(0, (current_node, weight))
                    path = self.reconstruct_ucs_path(predecessor, path)
        return path

# --- UCS --- UCS --- UCS --- UCS --- UCS --- UCS --- UCS --- UCS --- UCS --- UCS --- UCS ---
    def ucs(self, start_node, goal_node):  # Uniform Cost Search
        visited_nodes = []  # list of all visited nodes (initially empty)
        # Initialize empty priorityQueue:
        pQueue = PriorityQueue()
        # visited_nodes.append(start_node) # Add the start node to the `visited_nodes` list
        # Enqueue the start_node and make its (weight = 0) (g(n) = 0):
        pQueue.put((0, start_node, None))

        while not pQueue.empty():
            item = pQueue.get()  # removes the least-cost item, a tuple: (weight, node)
            cumulative_weight = item[0] 
            current_node = item[1] #The node itself
            came_from = item[2] #The predecessor of the node

            self.expanded_nodes.append((cumulative_weight, current_node, came_from))
            # print(current_node, end=" ")

            # Check if we reached the goal_node:
            if current_node == goal_node:
                break #  we reached the goal ✅
            else:
                if current_node not in visited_nodes:
                    visited_nodes.append(current_node)
                    for successor in self.graphlist[current_node]:
                        # `successor` is a tuple of (weight, node)
                        weight = successor[0]
                        node = successor[1]
                        if node not in visited_nodes:
                            pQueue.put((weight + cumulative_weight, node, current_node))
                            # What I store in the pQueue: (weight, node, predecessor)

        # After getting out of the while loop, construct the path from start to goal:
        path = self.reconstruct_ucs_path(goal_node, [])
        print("PATH: ", path)
        


# ------------------------------ End Class Graph ------------------------------------


# g = Graph(graph)
# start_node = "A"
# goal_node = "M"

# print("--------------- BFS ---------------")
# g.bfs(start_node, goal_node) # (start_node, goal_node)
# print("Expanded Nodes: ", g.get_expanded_nodes())
# print("Path: ", g.get_path("G"))

# g.clear_expanded_nodes_and_predecessors()


# print("--------------- DFS ---------------")
# g.dfs(start_node, goal_node) # (start_node, goal_node)
# print("Expanded Nodes: ", g.get_expanded_nodes())
# print("Path: ", g.get_path("M"))

# g.clear_expanded_nodes_and_predecessors()

#  ---------------- Unifrom Cost Search (UCS) 👇 ----------------
# g = Graph(graph_weighted)
# g = Graph(weighted_graph_from_slides)
# start_node = "S"
# goal_node = "G"

print("--------------- UCS ---------------")
g = Graph(weighted_graph_from_slides)
start_node = "S"
goal_node = "G"
g.ucs(start_node, goal_node)  # (start_node, goal_node)
print("Expanded Nodes: ", g.get_expanded_nodes())
print("Note: expanded_nodes is a list of tuples, each tuple is: (cost, node, came_from)")
