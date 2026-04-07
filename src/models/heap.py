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

    def extract_min(self):
        if len(self.data) == 0:
            return None

        if len(self.data) == 1:
            return self.data.pop(0)

        root = self.data[0]
        self.data[0] = self.data.pop(0)

        self.heapify_down(0)

        return root

    def heapify_down(self, index):
        size = len(self.data)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.data[left][0] < self.data[smallest][0]:
                smallest = left

            if right < size and self.data[right][0] < self.data[smallest][0]:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest

            else:
                break

    def is_empty(self):
        return len(self.data) == 0