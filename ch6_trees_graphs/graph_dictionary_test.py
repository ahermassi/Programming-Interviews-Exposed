from collections import defaultdict
from graph_dictionary import add_edge, generate_edges, find_path, find_all_paths, find_shortest_path

if __name__ == '__main__':
    graph = defaultdict(list)

    add_edge(graph, 'a', 'c')
    add_edge(graph, 'b', 'c')
    add_edge(graph, 'b', 'e')
    add_edge(graph, 'c', 'a')
    add_edge(graph, 'c', 'b')
    add_edge(graph, 'c', 'd')
    add_edge(graph, 'c', 'e')
    add_edge(graph, 'd', 'c')
    add_edge(graph, 'e', 'c')
    add_edge(graph, 'e', 'b')

    print(generate_edges(graph))

    print("Path from b to a: ", find_path(graph, 'b', 'a'))  # b -> c -> a

    print("Path from a to f: ", find_path(graph, 'a', 'f'))

    print("All paths from b to a: ", find_all_paths(graph, 'b', 'e'))  # b -> c -> a AND b -> e -> c -> a

    print("Shortest path from b to a: ", find_shortest_path(graph, 'b', 'e'))
