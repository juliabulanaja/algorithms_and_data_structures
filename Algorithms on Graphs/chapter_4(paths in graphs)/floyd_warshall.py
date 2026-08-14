# In graph theory, the Floyd-Warshall (FW) algorithm is an All-Pairs Shortest Path (APSP) algorithm. This means it can find the shortest path between all pairs of nodes.
# The time complexity to run FW is 0(V3) which is ideal for graphs no larger than a couple hundred nodes.
import copy


def propagate_negative_cycles(
    memo: list[list[float]], next_memo: list[list[int]], total_nodes: int
) -> None:
    """Mark vertices that are part of a reachable negative cycle.

    In the Floyd-Warshall relaxation process, if a path from i to k and from k to j
    exists, then any route that would pass through k can potentially create a cycle
    with negative total weight. When that happens, the distance between i and j is
    set to negative infinity and the predecessor link is invalidated so callers can
    detect the presence of a negative cycle.
    """

    for k in range(total_nodes):
        for i in range(total_nodes):
            for j in range(total_nodes):
                if memo[i][k] != float('inf') and memo[k][j] != float('inf'):
                    memo[i][j] = float('-inf')
                    next_memo[i][j] = -1


def floyd_warshall(adj_matrix: list[list[float]]) -> tuple[list[list[float]], list[list[int]]]:
    """Compute all-pairs shortest paths using the Floyd-Warshall algorithm.

    Args:
        adj_matrix: Square adjacency matrix where `adj_matrix[i][j]` is the weight
            of the edge from node `i` to node `j`, or `float('inf')` if no edge
            exists. The diagonal should contain zero for nodes with no self-loop.

    Returns:
        A tuple `(distances, next_memo)` where:
            - `distances[i][j]` is the shortest-path distance from `i` to `j`.
            - `next_memo[i][j]` stores the next vertex after `i` on a shortest path
              to `j`, or `-1` if a reachable negative cycle is detected.
    """

    total_nodes = len(adj_matrix)
    memo = copy.deepcopy(adj_matrix)
    next_memo: list[list[int]] = [[None] * total_nodes for _ in range(total_nodes)]

    # Initialize next_memo for path reconstruction
    for i in range(total_nodes):
        for j in range(total_nodes):
            if memo[i][j] != float('inf'):
                next_memo[i][j] = j

    # Standard Floyd-Warshall Algorithm
    for k in range(total_nodes):
        for i in range(total_nodes):
            for j in range(total_nodes):
                if memo[i][k] != float('inf') and memo[k][j] != float('inf'):
                    memo[i][j] = memo[i][k] + memo[k][j]
                    next_memo[i][j] = next_memo[i][k]

    propagate_negative_cycles(memo, next_memo, total_nodes)

    return memo, next_memo


def reconstruct_path(
    start: int, end: int, next_memo: list[list[int]], memo: list[list[float]]
) -> list[int] | None:
    """Reconstruct a shortest path from ``start`` to ``end``.

    Args:
        start: The source vertex index.
        end: The destination vertex index.
        next_memo: The successor matrix produced by ``floyd_warshall``.
        memo: The shortest-distance matrix produced by ``floyd_warshall``.

    Returns:
        A list of vertex indices representing the shortest path from ``start`` to
        ``end``, or an empty list if no path exists, or ``None`` if a reachable
        negative cycle prevents valid reconstruction.
    """
    if memo[start][end] == float('inf'):
        return []

    path = [start]

    while start != end:
        start = next_memo[start][end]
        if start == -1:
            return None
        path.append(start)

    return path


if __name__ == "__main__":
    # n, m = map(int, input().split(' '))

    # adj_matrix = [[float('inf')] * n for _ in range(n)]
    # for i in range(n):
    #     adj_matrix[i][i] = 0

    # for _ in range(m):
    #     u, v, w = map(int, input().split(' '))
    #     adj_matrix[u][v] = w

    adj_matrix = [[0, 4, 1, 9],
                  [3, 0, 6, 11],
                  [4, 1, 0, 2],
                  [6, 5, -4, 0]] 

    distances, paths = floyd_warshall(adj_matrix)
    print(distances)