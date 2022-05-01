class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __str__(self, depth=0):
        for i in range(depth):
            print("\t", end=" ")
        
        print(f"👉 {self.value}")
        for child in self.children:
            child.__str__(depth+1)

    def addChild(self, value):
        self.children.append(Node(value))
