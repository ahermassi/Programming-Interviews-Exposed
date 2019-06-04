from graph_adjacency_matrix import Graph

if __name__ == '__main__':

    graph  = Graph(6)

    graph.set_vertex(0, 'a')
    graph.set_vertex(1, 'b')
    graph.set_vertex(2, 'c')
    graph.set_vertex(3, 'd')
    graph.set_vertex(4, 'e')
    graph.set_vertex(5, 'f')

    graph.set_edge('a', 'e', 10)
    graph.set_edge('a', 'c', 20)
    graph.set_edge('c', 'b', 30)
    graph.set_edge('b', 'e', 40)
    graph.set_edge('e', 'd', 50)
    graph.set_edge('f', 'e', 60)

    print("Vertices of the graph: ", graph.get_vertices())
    print("Edges of the graph: ", graph.get_edges())
    print("Adjacency matrix of the graph: ", graph.get_matrix())
