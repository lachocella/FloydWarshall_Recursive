import floyd
import sys

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])

if __name__ == '__main__':
    # compare performance of imperative and recursive implementation
    import timeit
    print("Imperative:")
    g = graph
    imp_time = timeit.timeit(lambda: floyd.floyd(g), number=1)
    print("Time:", imp_time)
    print("Recursive:")
    rec_time = timeit.timeit(lambda: floyd.floyd_recursion(graph), number=1)
    print("Time:", rec_time)

    faster = "Imperative" if imp_time < rec_time else "Recursive"
    print("Faster:", faster)
