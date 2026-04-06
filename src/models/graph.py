class Graph:
    def __init__(self):
         self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2, weight=1):
        self.adj_list[node1].append((node2, weight))