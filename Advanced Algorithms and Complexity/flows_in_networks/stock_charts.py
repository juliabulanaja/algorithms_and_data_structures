# python3
# Task. You’re in the middle of writing your newspaper’s end-of-year economics summary, and you’ve decided
# that you want to show a number of charts to demonstrate how different stocks have performed over the
# course of the last year. You’ve already decided that you want to show the price of 𝑛 different stocks,
# all at the same 𝑘 points of the year.
# A simple chart of one stock’s price would draw lines between the points (0, 𝑝𝑟𝑖𝑐𝑒0),(1, 𝑝𝑟𝑖𝑐𝑒1), . . . ,(𝑘 −
# 1, 𝑝𝑟𝑖𝑐𝑒𝑘−1), where 𝑝𝑟𝑖𝑐𝑒𝑖
# is the price of the stock at the 𝑖-th point in time.
# In order to save space, you have invented the concept of an overlaid chart. An overlaid chart is the
# combination of one or more simple charts, and shows the prices of multiple stocks (simply drawing a
# line for each one). In order to avoid confusion between the stocks shown in a chart, the lines in an
# overlaid chart may not cross or touch.
# Given a list of 𝑛 stocks’ prices at each of 𝑘 time points, determine the minimum number of overlaid
# charts you need to show all of the stocks’ prices.
from queue import Queue


def bfs(s: int, t: int, capacity: list) -> list:
    """Return the shortest augmenting path from s to t in the residual graph.

    The path is reconstructed by tracking predecessors during a BFS traversal,
    and an empty list is returned when no path exists.
    """
    total_nodes = len(capacity)
    prev = [None] * total_nodes
    visited = [False] * total_nodes

    q = Queue()
    q.put(s) 
    visited[s] = True

    while not q.empty():  
        node = q.get()

        if node == t:
            break

        for neighbor in range(total_nodes):
            if not visited[neighbor] and capacity[node][neighbor] > 0:
                visited[neighbor] = True
                prev[neighbor] = node
                q.put(neighbor)

    if not visited[t]:
        return []
    
    path = []
    current = t
    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()
    return path
    

def get_bottleneck(path: list, capacity: list):
    """Return the minimum residual capacity along the augmenting path.

    The function iterates over each edge in the path and finds the smallest
    available capacity value that can be pushed through the path.
    """
    min_capacity = float('inf')
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        current_capacity = capacity[u][v]
        if current_capacity < min_capacity:
            min_capacity = current_capacity
    return min_capacity


def update_capacity(bottleneck: int, path: list, capacity: list) -> None:
    """Augment the flow along a path by pushing the bottleneck value.

    For each edge in the residual graph along the path, reduce the forward
    residual capacity by the bottleneck and increase the reverse residual
    capacity by the same amount to represent the flow augmentation.
    """
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        capacity[u][v] -= bottleneck
        capacity[v][u] += bottleneck


def ford_fulkerson(s: int, t: int, capacity: list) -> int:
    """Compute the maximum flow from s to t using the Ford-Fulkerson algorithm.

    Repeatedly finds an augmenting path in the residual graph, determines the
    bottleneck capacity along that path, and updates the residual capacities until
    no augmenting path remains.
    """
    total_max_flow = 0

    while True:

        path = bfs(s, t, capacity)

        if not path:
            break

        bottleneck = get_bottleneck(path, capacity)
        update_capacity(bottleneck, path, capacity)
        total_max_flow += bottleneck

    return total_max_flow


if __name__ == "__main__":
    n, k = map(int, input().strip().split(" "))

    prices = []
    for _ in range(n):
        prices.append(list(map(int, input().split())))

    total_nodes = 2 * n + 2
    s = 0
    t = total_nodes - 1

    capacity = [[0] * total_nodes for _ in range(total_nodes)]
    for i in range(1, n + 1):
        capacity[s][i] = 1

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            i_strictly_above_j = True
            for t_idx in range(k):
                if prices[i][t_idx] <= prices[j][t_idx]:
                    i_strictly_above_j = False
                    break
                        
            if i_strictly_above_j:
                capacity[i + 1][n + j + 1] = 1

    for j in range(1, n + 1):
        capacity[n + j][t] = 1

    flow = ford_fulkerson(s, t, capacity)
    min_charts = n - flow
    print(min_charts)