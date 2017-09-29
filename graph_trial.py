from itertools import groupby
from operator import itemgetter

class Graph(object):

    def __init__(self, graph_dict=None):
        """ Initializes a graph object """
        if graph_dict is None:
            self.__graph_dict = {}
            self.graphdict = False

        else:
            self.__graph_dict = graph_dict
            self.graphdict = True


    def vertices(self):
        """ returns a list of vertices """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of the graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ Add a vertex to the graph """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        """ Add an edge between vertices vertex1 & vertex2 """
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append((vertex1, vertex2, weight))
        else:
            self.__graph_dict[vertex1] = [(vertex1, vertex2, weight)]

        if vertex1 != vertex2:
            if vertex2 in self.__graph_dict:
                self.__graph_dict[vertex2].append((vertex2, vertex1, weight))
            else:
                self.__graph_dict[vertex2] = [(vertex2, vertex1, weight)]

    def __generate_edges(self):
        """ Return all the edges in the graph without duplicates """
        edges = []
        for vertex in self.__graph_dict:
            for neighbor_vertex in self.__graph_dict[vertex]:
                if self.graphdict == True:
                    (v1,v2,w) = (vertex, neighbor_vertex[0], neighbor_vertex[1])
                else:
                    (v1,v2,w) = neighbor_vertex

                # check for duplicates
                if (v2,v1,w) not in edges:
                    edges.append((v1,v2,w))

        return edges

    def find_isolated_vertex(self):
        """ find isolated vertices in case of disconnected graphs """
        isolated = []
        for vertex in self.__graph_dict:
            if not self.__graph_dict[vertex]:
                isolated.append([vertex])

        return isolated

    def is_edge(self, v1, v2):
        """ returns the edge between vertices v1 & v2 otherwise none """
        for vertex in self.__graph_dict:
            if vertex == v1:
                for neighbor in self.__graph_dict[vertex]:
                    if isinstance(neighbor, tuple):
                        (n1, w) = neighbor
                    else:
                        n1 = neighbor
                    if v2 == n1:
                        return {v1, neighbor}
        return None

    def find_path(self): # works only for 1st vertex(hv to modify)
        visited = []
        edges = []
        vertices = self.vertices()
        for i in range(len(vertices)-1):
            if vertices[i] not in visited:
                visited.append(vertices[i])
            for j in range(len(vertices)):
                if vertices[j] not in visited:
                    visited.append(vertices[j])
                    edge = self.is_edge(vertices[i], vertices[j])
                    if edge:
                        edges.append(edge)

        return edges

    def make_set(self, parent, rank, v):
        """ """
        parent[v] = v
        rank[v] = 0

    def find_parent(self, parent, vertex):

        if parent[vertex] == vertex:
            return vertex

        return self.find_parent(parent, parent[vertex])

    def union(self, parent, rank, root1, root2):

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root1] = root2
            rank[root2] += 1

    def min_spanning_tree(self):
        edges = self.edges()
        vertices = self.vertices()
        final_result = {}
        result = []
        parent = {}
        rank = {}
        e_sorted = sorted(edges, key = lambda item: item[2] )
        # print "sorted list of edges"
        # print e_sorted
        for v in vertices:
            self.make_set(parent, rank, v)
        # print parent
        # print rank
        for e in e_sorted:
            v1 = e[0]
            v2 = e[1]
            x = self.find_parent(parent, v1)
            y = self.find_parent(parent, v2)
            if x != y:
                result.append((e[0],[(e[1], e[2])]))
                self.union(parent, rank, x, y)
        for item in sorted(result):
            final_result.setdefault(item[0], []).append(item[1])
        return final_result

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

def some_func(Graph):
    return Graph.weight_values()


if __name__ == "__main__":
    g = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": []
         }

    g1 = {"A": [("B", 15), ("D", 5), ("C", 10)],
          "B": [("A", 15), ("C", 3)],
          "C": [("B", 3), ("D", 3), ("A", 10)],
          "D": [("A", 5), ("C", 3)]
         }

graph = Graph()
graph.add_edge('a','b', 4)
graph.add_edge('a','f',2)
graph.add_edge('f','b',5)
graph.add_edge('c','b',6)
graph.add_edge('c','f',1)
graph.add_edge('f','e',4)
graph.add_edge('d','e',2)
graph.add_edge('d','c',3)
print graph.vertices()
print graph.edges()
print "Minimum spanning tree:-"
print graph.min_spanning_tree()
graph1 = Graph(g1)
print graph1.min_spanning_tree()








