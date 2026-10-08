# python3
# Task. The airline offers a bunch of flights and has a set of crews that can work on those flights. However,
# the flights are starting in different cities and at different times, so only some of the crews are able to
# work on a particular flight. You are given the pairs of flights and associated crews that can work on
# those flights. You need to assign crews to as many flights as possible and output all the assignments.
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



def ford_fulkerson(s: int, t: int, capacity: list, n: int) -> int:
    """Compute the maximum flow from s to t using the Ford-Fulkerson algorithm.

    Repeatedly finds an augmenting path in the residual graph, determines the
    bottleneck capacity along that path, and updates the residual capacities until
    no augmenting path remains.
    """
    original_capacity = [row[:] for row in capacity]

    while True:

        path = bfs(s, t, capacity)

        if not path:
            break

        bottleneck = get_bottleneck(path, capacity)
        update_capacity(bottleneck, path, capacity)

    connections = [-1] * n
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            crew_node = n + j
            if original_capacity[i][crew_node] == 1 and capacity[i][crew_node] == 0:
                connections[i - 1] = j

    return connections



if __name__ == "__main__":
    n, m = map(int, input().strip(). split(" ")) # the number of flights, the number of crews

    total_nodes = n + m + 2
    s = 0
    t = total_nodes - 1

    capacity = [[0] * total_nodes for _ in range(total_nodes)]

    for i in range(1, n + 1):
        capacity[s][i] = 1
    
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, m + 1):
            capacity[i][n + j] = row[j - 1]

    for j in range(1, m + 1):
        capacity[n + j][t] = 1

    
    result = ford_fulkerson(s, t, capacity, n)
    print(*(result))
