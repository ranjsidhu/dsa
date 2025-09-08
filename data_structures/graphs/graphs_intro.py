class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        print("--------- Printing graph starts ---------")
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
        print("--------- Printing graph ends ---------")

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        keys = self.adj_list.keys()
        if v1 in keys and v2 in keys:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        keys = self.adj_list.keys()
        if v1 in keys and v2 in keys:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        vertices = self.adj_list.keys()
        edges = self.adj_list[vertex]
        if vertex in vertices:
            for other_vertex in edges:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 1)

graph.print_graph()
