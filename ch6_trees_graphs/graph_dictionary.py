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
    """
    For each edge connecting source and destination, this function adds an entry to the dictionary with source as key
    and appending to sources' list as value
    :param graph: graph to update
    :param src: source node
    :param dst: destination node
    :return:
    """
    graph[src].append(dst)


def generate_edges(graph):
    """
    This function returns a list of the different edges of the graph
    :param graph: graph to traverse
    :return: list of edges
    """
    edges = []
    for node, adj_list in graph.items():
        for adj in adj_list:
            edges.append((node, adj))

    return edges


def find_path(graph, start, end, path=None):
    """
    This function returns the first possible path from start node to end node
    :param graph: graph to search
    :param start: start node
    :param end: end node
    :param path: list that holds the different nodes to hit in order to go from start to node
    :return: return the path list
    """
    if path is None:
        path = []

    path.append(start)

    if start == end:  # if end coincides with start, do nothing
        return path

    if end in graph[start]:  # end node is immediate neighbor of start node
        path.append(end)
        return path

    for adj in graph[start]:  # investigate paths that start from the immediate neighbors
        if adj not in path:  # if node hasn't been visited before
            return find_path(graph, adj, end, path)  # new path contains the already visited nodes

    return None  # if all nodes have been visited an no path was returned, no path is possible


def find_all_paths(graph, start, end, path=None):

    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]  # return a list of lists of paths
    all_paths = []
    for adj in graph[start]:  # investigate paths that start from the immediate neighbors
        if adj not in path:  # avoid cycles
            new_path = find_all_paths(graph, adj, end, path)
            for p in new_path:
                all_paths.append(p)
    return all_paths

