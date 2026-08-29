"""
# In this task you will solve the classical logistics problem called Travelling
# Salesman Problem: you are given the location of a depot and the location
# of a list of stores on a road network, and you need to find the shortest
# path for a truck to start in the depot, visit each of the stores to deliver
# the goods there, and return back to the depot.
# Task. Compute the length of the shortest path starting in the depot, visiting each store at least once and returning to the depot.
"""


def solve(adj_matrix: list, depot: int, start: int, stores: list, path=[]):
    if not stores:
        return adj_matrix[depot][start], []

    min_distance = float("inf")
    for neighbor in stores:
        if adj_matrix[depot][neighbor] == float("inf"):
            continue
        w = adj_matrix[depot][neighbor]
        new_subset = [s for s in stores if s != neighbor]
        result, path = solve(adj_matrix, neighbor, start, new_subset)
        if result + w < min_distance:
            min_distance = result + w
            best_path = path + [neighbor]

    return min_distance if min_distance != float("inf") else 0, best_path


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_matrix = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        adj_matrix[i][i] = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj_matrix[u - 1][v - 1] = w

    depot = 0
    stores = [i for i, s in enumerate(adj_matrix[depot]) if s != depot and s != float("inf")]
    result, path = solve(adj_matrix, depot, depot, stores)
    print(result, path)


    # inf = float("inf")
    # adj_matrix = [[0, 16, 11, 6], [8, 0, 13, 16], [4, 7, 0, 9], [5, 12, 2, 0]]
    # depot = 0
    # stores = [1, 2, 3]
    # result = solve(adj_matrix, depot, depot, stores)
    # print(result)   