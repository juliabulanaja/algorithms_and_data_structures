# Task. Compute the number of strongly connected components of a given directed graph with 𝑛 vertices and
# 𝑚 edges.

def tarjan(adj_list: list) -> int:
    """
    Find the number of strongly connected components in a directed graph using Tarjan's algorithm.
    
    Args:
        adj_list: Adjacency list representation of the graph.
    
    Returns:
        The number of strongly connected components.
    """
    total_nodes = len(adj_list)
    id_ = 0
    ids = [-1] * total_nodes
    low = [0] * total_nodes
    on_stack = [False] * total_nodes
    ssc_count = 0
    stack = []

    for i in range(total_nodes):
        if ids[i] == -1:    # if unvisited
            dfs(i, adj_list, ids, low, on_stack, stack, id_)
            ssc_count += 1
    return ssc_count


def dfs(at: int, adj_list: list, ids: list, low: list, on_stack: list, stack: list, id_: int) -> None:
    """
    Depth-first search for Tarjan's algorithm to find strongly connected components.
    
    Args:
        at: Current node index.
        adj_list: Adjacency list representation of the graph.
        ids: Array to store discovery IDs of nodes.
        low: Array to store the lowest discovery ID reachable from each node.
        on_stack: Array to track if a node is currently on the stack.
        stack: Stack of nodes in the current SCC search.
        id_: Current discovery ID counter.
    """
    stack.append(at)
    on_stack[at] = True
    id_ += 1
    ids[at] = low[at] = id_

    for neighbor in adj_list[at]:
        if ids[neighbor] == -1:     # if unvisited
            dfs(neighbor, adj_list, ids, low, on_stack, stack, id_)
        if on_stack[neighbor]:
            low[at] = min(low[at], low[neighbor])

    if ids[at] == low[at]:
        while True:
            node = stack.pop()
            low[node] = ids[at]
            if node == at:
                break
            
   
if __name__ == "__main__":
    n, m = list(map(int, input().split(' ')))
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split(' '))
        adj_list[u - 1].append(v - 1)

    ssc_count = tarjan(adj_list)
    print(ssc_count)
