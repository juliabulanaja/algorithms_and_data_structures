# python3
# Task. A tornado is approaching the city, and we need to evacuate the people quickly. There are several
# roads outgoing from the city to the nearest cities and other roads going further. The goal is to evacuate
# everybody from the city to the capital, as it is the only other city which is able to accomodate that
# many newcomers. We need to evacuate everybody as fast as possible, and your task is to find out
# what is the maximum number of people that can be evacuated each hour given the capacities of all
# the roads.
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
    n, m = map(int, input().strip().split(" "))
    s = 0
    t = n - 1

    capacity = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v, c = map(int, input().split(' '))
        capacity[u - 1][v - 1] += c

    result = ford_fulkerson(s, t, capacity)
    print(result)