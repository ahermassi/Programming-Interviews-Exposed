"""
Python 3 implementation of a graph using Adjacency List
"""


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)] # adjacency list is a list of lists, where each list
        # contains the
        # adjacents of one of the vertices

    def add_edge(self, src, dst):
        self.adj_list[src].append(dst)
        # As it is an undirected graph, add the source to the destination's list of adjacency
        self.adj_list[dst].append(src)

    def print_graph(self):
        for i in range(self.num_vertices):
            print("Adjacency list of vertex {} \n head ".format(i), end='')
            for node in self.adj_list[i]:
                print("-> {}".format(node), end='')
            print('\n')
