class Node:
    def __init__(self, label, weight: "int"):
        self.label = label
        self.weight = weight

    def __init__(self, label, weight: "int", predecessor: "Node"):
        self.label = label
        self.weight = weight
        self.predecessor = predecessor