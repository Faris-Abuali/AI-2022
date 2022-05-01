class MinHeap:
    def __init__(self, capacity):
        # makes list of length (capacity) and fill it with zeros
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def display(self):
        print(self.storage[0:self.size]) #print only the used part of the list
        return

    def get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def parent(self, index):
        return self.storage[self.get_parent_index(index)]

    def get_left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def left_child(self, index):
        return self.storage[self.get_left_child_index(index)]

    def get_right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def right_child(self, index):
        return self.storage[self.get_right_child_index(index)]

    def is_full(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def insert(self, data):
        if self.is_full():
            raise("Heap is full!")

        self.storage[self.size] = data
        self.size += 1
        # pass the index of the last newly added element
        self.heapify_up(self.size - 1)
        return

    # ---------------------- Iterative Approach ----------------------
    # def heapify_up(self):
    #     index = self.size - 1  #index of the freshly added element
    #     while self.has_parent(index) and self.parent(index) > self.storage[index]:
    #         parent_index = self.get_parent_index(index)
    #         self.swap(parent_index, index)
    #         index = parent_index

    # ---------------------- Recursive Approach ----------------------
    def heapify_up(self, index):
        if self.has_parent(index) and self.parent(index) > self.storage[index]:
            parent_index = self.get_parent_index(index)
            self.swap(parent_index, index)
            self.heapify_up(parent_index)

    # ------------------------------------------------------------------
    def remove_min(self):
        if (self.size == 0):
            raise("Heap is empty!")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapify_down(0) #start from the root heapifing down 
        return data
    # ---------------------- Iterative Approach ----------------------

    # def heapify_down(self):
    #     index = 0
    #     while self.has_left_child(index):
    #         # assume for now that the smaller child is the left child
    #         smaller_child_index = self.get_left_child_index(index)
    #         if (self.has_right_child(index) and self.right_child(index) < self.left_child(index)):
    #             smaller_child_index = self.get_right_child_index(index)
    #         # Now am sure that I'm storing the index of the smaller child.
    #         if (self.storage[index] < self.storage[smaller_child_index]):
    #             # then the min heap is preserved, since every parent node must be smaller than its children nodes
    #             break
    #         else:
    #             self.swap(index, smaller_child_index)
    #             index = smaller_child_index
                
    # ---------------------- Recursive Approach ----------------------
    def heapify_down(self, index):
        smallest_index = index
        if self.has_left_child(index) and self.storage[smallest_index] > self.left_child(index):
            smallest_index = self.get_left_child_index(index)
        if self.has_right_child(index) and self.storage[smallest_index] > self.right_child(index):
            smallest_index = self.get_right_child_index(index)
        if smallest_index != index:
            self.swap(index, smallest_index)
            self.heapify_down(smallest_index)

                
