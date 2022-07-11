import itertools
import sys

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH),
                                                                range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate] + distance[intermediate][end_node])
    # Any value that have sys.maxsize has no path
    return distance


# recursive function to obtain the path as a string
def get_path(i, j, graph, parent):
    if graph[i][j] == NO_PATH:
        return " no path to "
    if parent[i][j] == i:
        return " "
    else:
        return get_path(i, parent[i][j], graph, parent) + str(parent[i][j] + 1) + \
               get_path(parent[i][j], j, graph, parent)


def floyd_recursion(graph):
    # no of vertices
    v = len(graph)

    parent = []

    # initialize
    for i in range(0, v):
        parent.append([])
        for j in range(0, v):
            parent[i].append(0)

    # path from vertex to itself is set to 0
    for i in range(0, v):
        graph[i][i] = 0

    # initialize the path matrix
    for i in range(0, v):
        for j in range(0, v):
            if graph[i][j] == NO_PATH:
                parent[i][j] = 0
            else:
                parent[i][j] = i

    # actual floyd warshall algorithm
    for k in range(0, v):
        for i in range(0, v):
            for j in range(0, v):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    parent[i][j] = parent[k][j]

    # check for negative cycles
    for i in range(0, v):
        if graph[i][i] != 0:
            print("Negative cycle detected: ", i + 1)
            sys.exit()

    # matrix for final distances
    paths = []

    # display shortest paths
    for i in range(0, v):
        paths.append([])
        for j in range(0, v):
            paths[i].append(str(i + 1) + get_path(i, j, graph, parent) + str(j + 1) + " => (" + str(graph[i][j]) + ")")

    return paths


print("\n\n\n")
print("Floyd Warshall Algorithm (Imperative)")
print(floyd(graph))

print("\n\n\n")
print("Floyd Warshall Algorithm (Recursive)")
print(floyd_recursion(graph))
