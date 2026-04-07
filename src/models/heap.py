class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.data[index][0] < self.data[parent][0]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break