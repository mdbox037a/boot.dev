class Graph:
    def __init__(self):
        pass

    def add_edge(self, u, v):
        pass

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
