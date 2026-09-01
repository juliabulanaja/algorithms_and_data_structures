# An Eulerian path is a continuous trail in a graph that visits every edge exactly once.


def find_eulerian_path(adj_list: list[list[int]]) -> list[int] | None:
    """Return an Eulerian path for a directed graph if it exists.

    A directed Eulerian trail exists when every vertex has balanced in/out degree,
    or exactly one vertex has outdegree = indegree + 1 and one vertex has
    indegree = outdegree + 1. The traversal starts at the unique vertex with
    excess outdegree (or any vertex in an Eulerian circuit) and ends at the unique
    vertex with excess indegree.

    Args:
        adj_list: Adjacency list of a directed graph, where adj_list[u] contains
            the neighbors reachable from vertex u.

    Returns:
        A list of vertices describing an Eulerian path, or None if no such path
        exists.
    """

    start = None
    total_vertices = len(adj_list)
    total_edges = 0
    outdegree = [0] * total_vertices
    indegree = [0] * total_vertices
    path = []

    for v, edges in enumerate(adj_list):
        for neighbor in edges:
            indegree[neighbor] += 1
            outdegree[v] += 1
            total_edges += 1

    start_nodes = 0
    end_nodes = 0

    for i in range(total_vertices):
        if outdegree[i] - indegree[i] > 1 or indegree[i] - outdegree[i] > 1:
            return None
        elif outdegree[i] - indegree[i] == 1:
            start_nodes += 1
            start = i 
        elif indegree[i] - outdegree[i] == 1:
            end_nodes += 1
        elif indegree[i] == outdegree[i]:
            continue

    if (start_nodes, end_nodes) not in [(0, 0), (1, 1)]:
        return None

    if start is None:
        start = 0

    dfs(start, adj_list, outdegree, path)

    if len(path) == total_edges + 1:
        path.reverse()
        return path
    return None


def dfs(start: int, adj_list: list[list[int]], outdegree: list[int], path: list[int]):
    """Depth-first postorder traversal that reconstructs an Eulerian trail.

    This helper follows outgoing edges in reverse order of the current adjacency
    list, appending vertices after exploring all remaining outgoing edges from a
    node. The result is then reversed in the caller to produce the Eulerian path.
    """
    
    while outdegree[start] > 0:
        outdegree[start] -= 1
        neighbor = adj_list[start][outdegree[start]]
        dfs(neighbor, adj_list, outdegree, path)

    path.append(start)


if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        i, j = map(int, input().split(" "))
        adj_list[i].append(j)

    result = find_eulerian_path(adj_list)
    print(result)
    