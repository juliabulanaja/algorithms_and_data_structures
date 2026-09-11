# Task. The goal of the maximum flow problem is to determine the maximum volume of traffic, data, or fluid that can pass from a source node to a sink node through a capacity-constrained network.
from queue import Queue


def bfs(s: int, t: int, capacity: list[list[int]]) -> list:
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
    

def get_bottleneck(path: list[int], capacity: list[list[int]]):
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


def update_capacity(bottleneck: int, path: list[int], capacity: list[list[int]]) -> None:
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


def ford_fulkerson(s: int, t: int, capacity: list[list[int]]) -> int:
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

    n, m = map(int, input().split(" "))
    s, t = map(int, input().split(" "))

    capacity = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v, c = map(int, input().split(" "))
        capacity[u - 1][v - 1] = c

    result = ford_fulkerson(s - 1, t - 1, capacity)
    print(result)
