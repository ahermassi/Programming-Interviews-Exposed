# a -> c
# b -> c
# b -> e
# c -> a
# c -> b
# c -> d
# c -> e
# d -> c
# e -> c
# e -> b

# The graph can be represented using the following dictionary:
# graph = { "a" : ["c"],
#           "b" : ["c", "e"],
#           "c" : ["a", "b", "d", "e"],
#           "d" : ["c"],
#           "e" : ["c", "b"],
#           "f" : []
#         }
from collections import defaultdict


def add_edge(graph, src, dst):
    graph[src].append(dst)


def generate_edges(graph):
    edges = []
    for node, adj_list in graph.items():
        for adj in adj_list:
            edges.append((node, adj))

    return edges


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

