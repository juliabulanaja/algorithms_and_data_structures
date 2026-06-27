# Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle.

class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []
        self.visited = 0

    def __str__(self):
        return f"{self.value}: [{', '.join(str(item) for item in self.connections)}]"


class Graph:
    def __init__(self, m):
        self.n = n
        self.nodes = []

    def __str__(self):
        return '\n'.join(str(node) for node in self.nodes)


    def get_node_index(self, value):
        if not len(self.nodes):
            return None

        left = 0
        right = len(self.nodes)

        while left <= right:
            m = (right + left) // 2
            middle = self.nodes[m]

            if middle.value == value:
                return m
            elif middle.value > value:
                right = m - 1      
            else:
                left = m + 1


    def initialize(self, edges):
        for i in range(self.n):
            node = Node(i+1)
            self.nodes.append(node)

        for value, connection in edges:
            node_index = self.get_node_index(value)
            node = self.nodes[node_index]
            if node:
                node.connections.append(connection)
            

    def has_cycle(self):

        states = [0] * len(self.nodes) # 0 - not sink, 1 - visiting, 2 - is a sink

        def is_sink(node_index):

            state = states[node_index]
            node = self.nodes[node_index]


            if state == 0:
                states[node_index] = 1
            elif state == 1:
                return False
            else: # state == 2:
                return True # it is a sink

            n_connections = node.connections  

            if not n_connections:
                states[node_index] = 2
                return True # it is a sink

            results = []

            for c in n_connections:
                c_index = self.get_node_index(c)
                is_sink_ = is_sink(c_index)
                results.append(is_sink_)

            if all(results):
                states[node_index] = 2
                return True # it is a sink

        for i in range(self.n):
            is_sink(i)

        if all(x == 2 for x in states):
            print(0)
        else:
            print(1)


if __name__ == "__main__":
    n, m = list(map(int, input().split(' ')))
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split(' '))))

    graph = Graph(n)
    graph.initialize(edges)
    # print(graph)
    graph.has_cycle()



