"""
Python 3 implementation of a graph using Adjacency Matrix
"""


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[-1] * num_vertices for _ in range(num_vertices)]
        self.vertices = {}
        self.vertices_list = [0] * num_vertices

    def set_vertex(self, vertex, vertex_id):
        if vertex in range(self.num_vertices + 1):
            self.vertices_list[vertex] = vertex_id  # set_vertex(0, 'a') results in vertices_list[0] = 'a'
            self.vertices[vertex_id] = vertex  # set_vertex(0, 'a') results in an entry {'a': 0} in the dictionary

    def set_edge(self, frm, to, cost=0):
        from_vertex = self.vertices[frm]
        to_vertex = self.vertices[to]

        self.adj_matrix[from_vertex][to_vertex] = cost

        #  Adjacency matrix of an undirected graph is symmetric
        self.adj_matrix[to_vertex][from_vertex] = cost

    def get_vertices(self):
        return self.vertices_list

    def get_edges(self):
        """
        This method returns a list of tuples.
        For example, if there is an edge 'a' -> 'b' of cost 10, edges list contains a tuple ('a', 'b', 10).
        vertices_list is used as a mapping from a vertex position in adjacency matrix to actual vertex name.
        :return:
        """
        edges = [(self.vertices_list[i], self.vertices_list[j], self.adj_matrix[i][j])
                 for i in range(self.num_vertices)
                 for j in range(self.num_vertices)
                 if self.adj_matrix[i][j] != -1]

        return edges

    def get_matrix(self):
        return self.adj_matrix
