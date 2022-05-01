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
    
        def clear_expanded_nodes(self):
            self.expanded_nodes.clear()

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

# --- After implementing the DLS, we can implement the Iterative Deepening Search algorithm, making use of the same dls() function we used to implement the DLS (Depth-Limited Search): ---
    def iterative_deepining_search(self, start_node, goal_node, stop, step):
        found = False
        for i in range(0, stop, step):
            found = self.dls(start_node, goal_node, i)
            print(self.get_expanded_nodes())
            self.clear_expanded_nodes()
            if found: break
        return found
# ---------------------------------- End Class Graph -------------------------------------