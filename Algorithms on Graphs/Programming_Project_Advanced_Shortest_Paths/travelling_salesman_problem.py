# In this task you will solve the classical logistics problem called Travelling
# Salesman Problem: you are given the location of a depot and the location
# of a list of stores on a road network, and you need to find the shortest
# path for a truck to start in the depot, visit each of the stores to deliver
# the goods there, and return back to the depot.
# Task. Compute the length of the shortest path starting in the depot, visiting each store at least once and
# returning to the depot.
import heapq
from itertools import combinations


def witness_path(start_node: int, adj_list: list, node_to_avoid: int = None, contracted: list = None, distance_limit: float = None, node_limit: int = 100) -> list:
    """Find shortest witness paths from a node using a bounded Dijkstra search.

    A witness path is an alternative path that does not pass through the
    node currently being contracted. If such a path is no longer than the
    path through the contracted node, a shortcut is not required.

    Args:
        start_node: Starting vertex for the Dijkstra search.
        adj_list: Forward adjacency list of the graph.
        node_to_avoid: Vertex that must not be traversed during the search.
        contracted: Boolean list indicating which vertices have already
            been contracted.
        distance_limit: Maximum distance that the search is allowed to
            explore.
        node_limit: Maximum number of vertices that may be processed.

    Returns:
        A dictionary mapping each reached vertex to its shortest distance
        from start_node within the search limits.
    """
    
    total_nodes = len(adj_list)
    distances = {start_node: 0}
    nodes_processed = 0

    queue = [(0, start_node)]
    while queue:
        d, current_node = heapq.heappop(queue)

        if d > distances[current_node]:
            continue

        if distance_limit is not None and d > distance_limit:
            break

        nodes_processed += 1

        if node_limit is not None and nodes_processed > node_limit:
            break

        for neighbor, w in adj_list[current_node]:

            if node_to_avoid is not None and neighbor == node_to_avoid:
                continue

            if contracted is not None and contracted[neighbor]:
                continue

            new_distance = d + w

            if new_distance < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances


def calculate_node_priority(node: int, adj_list: list, adj_list_reversed: list, contracted: list[bool]) -> float:
    """Calculate the contraction priority of a vertex.

    The priority combines the number of required shortcuts, the edge
    difference, and the number of already contracted neighbors. Lower
    priority vertices are preferred for contraction.

    Args:
        node: Vertex whose priority is being calculated.
        adj_list: Forward adjacency list of the graph.
        adj_list_reversed: Reversed adjacency list of the graph.
        contracted: Boolean list indicating which vertices have already
            been contracted.

    Returns:
        The calculated priority of the vertex.
    """

    incoming_nodes = [
        edge for edge in adj_list_reversed[node]
        if not contracted[edge[0]]
    ]

    outcoming_nodes = [
        edge for edge in adj_list[node]
        if not contracted[edge[0]]
    ]

    edges_removed = len(incoming_nodes) + len(outcoming_nodes)
    shortcuts = 0
    if incoming_nodes and outcoming_nodes:
        for in_edge, d_in in incoming_nodes:
            max_distance = max(
                d_in + d_out
                for _, d_out in outcoming_nodes
            )

            distances = witness_path(
                in_edge,
                adj_list,
                node_to_avoid=node,
                contracted=contracted,
                distance_limit=max_distance
            )

            for out_edge, d_out in outcoming_nodes:

                if in_edge == out_edge:
                    continue

                direct_distance = d_in + d_out

                if out_edge not in distances or distances[out_edge] > direct_distance:
                    shortcuts += 1

    contracted_neighbors = sum(
        contracted[v]
        for v, _ in adj_list[node]
    )

    contracted_neighbors += sum(
        contracted[v]
        for v, _ in adj_list_reversed[node]
    )

    edge_difference = shortcuts - edges_removed
    return shortcuts + edge_difference + contracted_neighbors


def update_edge(node: int, neighbor: int, new_weight: float, adj_list: list, adj_list_reversed: list) -> None:
    """Add a directed edge to both forward and reversed adjacency lists.

    Args:
        node: Source vertex of the new edge.
        neighbor: Destination vertex of the new edge.
        new_weight: Weight of the new edge.
        adj_list: Forward adjacency list to update.
        adj_list_reversed: Reversed adjacency list to update.

    Returns:
        None.
    """

    adj_list[node].append([neighbor, new_weight])
    adj_list_reversed[neighbor].append([node, new_weight])


def contraction(initial_graph: list, initial_graph_reversed: list) -> tuple[list, list, list, dict]:
    """Preprocesses a graph by contracting vertices according to dynamic priorities.

    Iteratively contracts non-contracted nodes with the lowest priority score. During 
    contraction, shortcuts are inserted between neighboring nodes if the shortest path 
    through the contracted node is strictly shorter than any witness path.

    Args:
        initial_graph: Adjacency list of the original forward graph, where each edge 
            is formatted as `[neighbor, weight]`.
        initial_graph_reversed: Adjacency list of the original reversed graph, where 
            each edge is formatted as `[predecessor, weight]`.

    Returns:
        A tuple containing four elements:
            - augmented_graph (list): Forward adjacency list containing both original 
              and newly inserted shortcut edges.
            - augmented_graph_reversed (list): Reversed adjacency list containing both 
              original and newly inserted shortcut edges.
            - final_priorities (list[int]): Contraction order/rank assigned to each node 
              (0-indexed by order of contraction).
            - shortcuts_history (dict): Mapping of edge tuples `(u, v)` to their intermediate 
              contracted node `mid` for shortcut unpacking.
    """

    total_nodes = len(initial_graph)

    augmented_graph = [[list(edge) for edge in edges] for edges in initial_graph]
    augmented_graph_reversed = [[list(edge) for edge in edges] for edges in initial_graph_reversed]

    final_priorities = [0] * total_nodes
    contracted = [False] * total_nodes
    contracted_order_index = 0

    shortcuts_history = dict()

    queue = []
    for node in range(total_nodes):
        pri = calculate_node_priority(node, augmented_graph, augmented_graph_reversed, contracted)
        heapq.heappush(queue, (pri, node))

    while queue:

        current_priority, current_node = heapq.heappop(queue)
        if contracted[current_node]:
            continue
       
        new_pri = calculate_node_priority(current_node, augmented_graph, augmented_graph_reversed, contracted)
        if queue and new_pri > queue[0][0]:
            heapq.heappush(queue, (new_pri, current_node))
            continue

        contracted[current_node] = True
        final_priorities[current_node] = contracted_order_index
        contracted_order_index += 1

        incoming_nodes = [
            edge
            for edge in augmented_graph_reversed[current_node]
            if not contracted[edge[0]]
        ]

        outcoming_nodes = [
            edge
            for edge in augmented_graph[current_node]
            if not contracted[edge[0]]
        ]

        if not incoming_nodes or not outcoming_nodes:
            continue

        shortcuts_to_add = []

        for in_edge, _ in incoming_nodes:
            if (in_edge, current_node) not in shortcuts_history:
                shortcuts_history[(in_edge, current_node)] = None
        for out_edge, _ in outcoming_nodes:
            if (current_node, out_edge) not in shortcuts_history:
                shortcuts_history[(current_node, out_edge)] = None

        for in_edge, d in incoming_nodes:  
            max_distance = max(
                d + outgoing_weight
                for _, outgoing_weight in outcoming_nodes
            )
            undirect_distance = witness_path(in_edge, augmented_graph, current_node, contracted=contracted, distance_limit=max_distance)
          
            for out_edge, d_ in outcoming_nodes:
                if in_edge == out_edge:
                    continue

                direct_distance = d + d_

                if (out_edge not in undirect_distance) or undirect_distance[out_edge] > direct_distance:
                    shortcuts_to_add.append(
                        (in_edge, out_edge, direct_distance)
                    )

        for in_edge, out_edge, distance in shortcuts_to_add:
            update_edge(in_edge, out_edge, distance, augmented_graph, augmented_graph_reversed)
            shortcuts_history[(in_edge, out_edge)] = current_node

    return augmented_graph, augmented_graph_reversed, final_priorities, shortcuts_history


def calculate_distance(start_node: int, target_node: int, preprocessed_graph: list, preprocessed_graph_reversed: list, priorities: list) -> (float, list):
    """Calculates the shortest distance and contracted path using Contraction Hierarchies.

    Executes a bidirectional Dijkstra search restricted to upward edges (edges leading 
    to vertices with higher contraction ranks). Reconstructs the middle meeting point 
    and constructs the shortcut-level path between source and target.

    Args:
        start_node: Source vertex ID.
        target_node: Destination vertex ID.
        preprocessed_graph: Forward graph adjacency list containing original and 
            shortcut edges.
        preprocessed_graph_reversed: Backward/reversed graph adjacency list containing 
            original and shortcut edges.
        priorities: Contraction rank assigned to each vertex.

    Returns:
        A tuple containing:
            - best_distance (float | int): Shortest-path distance from `start_node` to 
              `target_node`, or `float('inf')` if unreachable.
            - path_with_shortcuts (list[int]): Ordered sequence of node IDs along the 
              shortest path before unpacked shortcuts (includes shortcut hops).
    """

    total_nodes = len(priorities)

    distances = [float("inf")] * total_nodes
    distances_reversed = [float("inf")] * total_nodes
    distances[start_node] = 0
    distances_reversed[target_node] = 0

    processed = [False] * total_nodes
    processed_reversed = [False] * total_nodes

    best_distance = float("inf")
    meeting_node = None

    queue = [(0, start_node)]
    queue_reversed = [(0, target_node)]

    prev_fwd = [None] * total_nodes
    prev_rev = [None] * total_nodes

    while queue or queue_reversed:

        if queue:
            d, node = heapq.heappop(queue)
            if processed[node]:
                continue
            processed[node] = True

            if distances[node] <= best_distance:
                for neighbor, w in preprocessed_graph[node]:
                    if priorities[neighbor] > priorities[node] and not processed[neighbor]:
                        if distances[neighbor] > distances[node] + w:
                            distances[neighbor] = distances[node] + w
                            prev_fwd[neighbor] = node
                            heapq.heappush(queue, (distances[neighbor], neighbor))

            if processed_reversed[node] and distances[node] + distances_reversed[node] < best_distance:
                best_distance = distances[node] + distances_reversed[node]
                meeting_node = node

        if queue_reversed:
            d_r, node_r = heapq.heappop(queue_reversed)
            if processed_reversed[node_r]:
                continue
            processed_reversed[node_r] = True

            if distances_reversed[node_r] <= best_distance:
                for neighbor, w in preprocessed_graph_reversed[node_r]:
                    if priorities[neighbor] > priorities[node_r] and not processed_reversed[neighbor]:
                        if distances_reversed[neighbor] > distances_reversed[node_r] + w:
                            distances_reversed[neighbor] = distances_reversed[node_r] + w
                            prev_rev[neighbor] = node_r
                            heapq.heappush(queue_reversed, (distances_reversed[neighbor], neighbor))

            if processed[node_r] and distances_reversed[node_r] + distances[node_r] < best_distance:
                best_distance = distances[node_r] + distances_reversed[node_r]
                meeting_node = node_r

    if meeting_node is None or best_distance == float("inf"):
        return float("inf"), []

    path_with_shortcuts = get_path_between_two_nodes(meeting_node, prev_fwd, prev_rev)

    return best_distance, path_with_shortcuts


def create_distance_matrix(stores: list, preprocessed_graph: list, preprocessed_graph_reversed: list, priorities: list) -> (list, list):
    """Computes pairwise shortest distances and paths between a list of target locations.

    Uses Contraction Hierarchies bidirectional search to build an all-pairs 
    distance and path lookup table for the specified subset of graph nodes.

    Args:
        stores: List of node IDs representing the target locations (e.g., depot and stores).
        preprocessed_graph: Forward graph adjacency structure after node contraction.
        preprocessed_graph_reversed: Reverse graph adjacency structure after node contraction.
        priorities: Contraction hierarchy priority/rank ordering for each node.

    Returns:
        A tuple containing:
            - dist_matrix (list[list[int]]): 2D list where `dist_matrix[i][j]` is the 
              shortest distance between `stores[i]` and `stores[j]`.
            - path_matrix (list[list[list[int] | None]]): 2D list where `path_matrix[i][j]` 
              is the unpacked node path from `stores[i]` to `stores[j]`.
    """

    total_stores = len(stores)
    dist_matrix = [[0] * total_stores for _ in range(total_stores)]
    path_matrix = [[None] * total_stores for _ in range(total_stores)]

    for i, store in enumerate(stores):
        for j, other_store in enumerate(stores):
            if store != other_store:
                d, path = calculate_distance(store, other_store, preprocessed_graph, preprocessed_graph_reversed, priorities)
                dist_matrix[i][j] = d
                path_matrix[i][j] = path
    return dist_matrix, path_matrix


def create_bitmask(visited_indices: list[int]) -> int:
    """Converts a collection of visited node indices into an integer bitmask.

    Each index sets the corresponding bit position to 1 (e.g., index 3 sets 2^3).
    Useful for tracking visited states in dynamic programming and graph traversals.

    Args:
        visited_indices: An iterable of 0-based node or element indices.

    Returns:
        An integer where each set bit represents a visited index.
    """

    mask = 0
    for idx in visited_indices:
        mask |= 1 << idx
    return mask


def held_karp(dist_matrix: list[list]) -> (float, list):
    """Computes the minimum Travelling Salesperson Problem (TSP) tour cost using bitmask DP.

    Implements the Held-Karp dynamic programming algorithm to solve the exact TSP 
    over a set of nodes starting and ending at index 0 (depot).

    Args:
        dist_matrix: Square 2D list where `dist_matrix[i][j]` represents the distance 
            or cost to travel from node `i` to node `j`.

    Returns:
        A tuple containing:
            - min_distance (float | int): The minimum total cost of a complete 
              Hamiltonian cycle visiting all nodes and returning to node 0. Returns 
              `float('inf')` if any pair is unreachable.
            - memo (list[list[float]]): The 2D dynamic programming lookup table of size 
              `2^N x N`, where `memo[mask][v]` holds the minimum cost to visit the 
              subset of nodes in `mask` ending at node `v`.

    Notes:
        - Assumes nodes are 0-indexed from `0` to `N - 1`, with node `0` acting as the origin.
        - Time Complexity: O(N^2 * 2^N)
        - Space Complexity: O(N * 2^N)
    """

    total_stores = len(dist_matrix)
    for row in dist_matrix:
        if float('inf') in row:
            return float('inf'), []

    memo = [[float("inf")] * total_stores for _ in range(1 << total_stores)]

    # base case
    for i in range(1, total_stores):
        mask = create_bitmask([i, 0])
        memo[mask][i] = dist_matrix[0][i]

    # populate 2D memo grid
    for size in range(2, total_stores):
        for mask in range(1 << total_stores):

            # if size = 1, it only looks at binary masks like 001, 010, 100
            if bin(mask).count("1") != size: 
                continue

            for last in range(total_stores):
                if last == 0:
                    continue

                cost_so_far = memo[mask][last]
                if cost_so_far == float("inf"):
                    continue

                for nxt in range(total_stores):
                    
                    if (mask & (1 << nxt)) != 0:  # If already visited
                        continue

                    next_mask = mask | (1 << nxt)
                    new_cost = cost_so_far + dist_matrix[last][nxt]

                    if new_cost < memo[next_mask][nxt]:
                        memo[next_mask][nxt] = new_cost

    min_distance = float('inf')
    for i in range(1, total_stores):
        cost_so_far = memo[-1][i]
        end_distance = dist_matrix[i][0] + cost_so_far
        if end_distance < min_distance:
            min_distance = end_distance 
    
    return min_distance, memo


def get_path_between_two_nodes(meeting_node: int, prev_fwd: list, prev_rev: list) -> list[int]:
    """Reconstructs the contracted path between source and target nodes using search predecessors.

    Traces backward from the bidirectional Dijkstra meeting point to the source via 
    `prev_fwd`, and forward from the meeting point to the target via `prev_rev`.

    Args:
        meeting_node: The vertex ID where the forward and reverse search trees met. 
            Returns an empty list if `None`.
        prev_fwd: Predecessor array from the forward search, mapping each node 
            to its parent along the path from the source.
        prev_rev: Predecessor array from the reverse search, mapping each node 
            to its parent along the path to the target.

    Returns:
        Ordered list of vertex IDs forming the path (including shortcut edges) 
        from source to target. Returns an empty list if no valid meeting node exists.
    """
    if meeting_node is None:
        return []

    path_fwd = []
    curr = meeting_node

    while curr is not None:
        path_fwd.append(curr)
        curr = prev_fwd[curr]
    path_fwd.reverse()

    path_rev = []
    curr = prev_rev[meeting_node]

    while curr is not None:
        path_rev.append(curr)
        curr = prev_rev[curr]

    full_path_with_shortcuts = path_fwd + path_rev
    return full_path_with_shortcuts


def unpack_edge(u: int, v: int, shortcuts_history: dict) -> list[int]:
    """Recursively unpacks a Contraction Hierarchy edge into its original node path.

    Note that the start node `u` is excluded from the returned list to facilitate 
    clean concatenation across adjacent path segments without duplicating endpoints.

    Args:
        u: The starting node ID of the edge.
        v: The ending node ID of the edge.
        shortcuts_history: Mapping of shortcut tuples `(start, end)` to their
            intermediate contracted node `mid`.

    Returns:
        A list of node IDs forming the subpath from `u` to `v`, including `v` 
        and any intermediate nodes, but excluding `u`.
    """

    # check if (u, v) is a shortcut edge
    mid = shortcuts_history.get((u, v))
    
    # no intermediate node
    if mid is None:
        return [v]
    
    # unpack left sub-edge (u -> mid) and right sub-edge (mid -> v)
    return unpack_edge(u, mid, shortcuts_history) + unpack_edge(mid, v, shortcuts_history)


def reconstract_path(memo: list, dist_matrix: list[list], path_matrix: list[list], min_distance: float, depot: int, stores: list, shortcuts_history: list) -> list[int]:
    """Reconstructs the complete node-level TSP tour using DP state tracing and shortcut unpacking.

    Traces back through the Held-Karp dynamic programming lookup table (`memo`) to find 
    the sequence of visited stores, then unpacks all Contraction Hierarchy shortcuts 
    into a fully resolved path of original 1-based node IDs.

    Args:
        memo: 2D dynamic programming lookup table from the Held-Karp algorithm.
        dist_matrix: Pairwise distance matrix between the depot and target stores.
        path_matrix: Pairwise path lookup table between target locations.
        min_distance: Total optimal tour cost returned by the TSP solver.
        depot: 0-based node ID of the depot/starting location.
        stores: List of 0-based node IDs of stores to be visited.
        shortcuts_history: Mapping of shortcut tuples `(u, v)` to intermediate 
            contracted nodes for path expansion.

    Returns:
        List of 1-based node IDs representing the full step-by-step route starting 
        and ending at the depot. Returns an empty list if no valid path exists.
    """

    next_mask = len(memo) - 1      # 1111
    q = [(min_distance, 0, next_mask, [])]   # (remaining_distance, prev_node, current_mask, path_indices)
    store_path = []

    while q:
        min_distance, prev_node, mask, path = heapq.heappop(q)  #   23, 0, 1111, []
        if len(path) == len(stores) and dist_matrix[0][prev_node] == min_distance:
            store_path = [0] + [i for i in reversed(path)] + [0]
            break

        for i, dist in enumerate(memo[mask]):
            if dist == float('inf') or i in path:
                continue
            if dist + dist_matrix[i][prev_node] == min_distance:
                next_mask = mask & ~(1 << i)
                heapq.heappush(q, (dist, i, next_mask, path + [i]))

    if not store_path:
        return []

    stores = [depot] + stores
    full_path = [depot]

    for i in range(len(store_path) - 1):

        start_node = stores[store_path[i]]
        target_node = stores[store_path[i + 1]]

        local_path = unpack_edge(start_node, target_node, shortcuts_history)
        full_path.extend(local_path)

    return [i + 1 for i in full_path]


def solve(adj_list: list, depot: int, start: int, stores: list, memo=None):
    """
    Solve the travelling salesman problem using dynamic programming.
    
    Args:
        adj_list: Adjacency list representation of the graph.
        depot: Starting depot node.
        start: Current starting node.
        stores: List of stores to visit.
        memo: Memoization dictionary to cache results.
    
    Returns:
        Minimum distance to visit all stores and return to depot.
    """
    if memo is None:
        memo = {}

    state = (depot, tuple(sorted(stores)))
    if state in memo:
        return memo[state]

    if not stores:
        result, path = calculate_distance(depot, start, preprocessed_graph, preprocessed_graph_reversed, priorities)
        return result, path

    min_distance = float("inf")
    for neighbor in stores:
        w, path = calculate_distance(depot, neighbor, preprocessed_graph, preprocessed_graph_reversed, priorities)
        if w < float("inf"):
            new_subset = [s for s in stores if s != neighbor]
            result = solve(adj_list, neighbor, start, new_subset, memo)
            new_distance = w + result

            if new_distance < min_distance:
                min_distance = new_distance
    memo[state] = min_distance

    return min_distance


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n)]
    adj_list_reversed = [[] for _ in range(n)]
    for _ in range(m):
        i, j, l = map(int, input().split(" "))
        adj_list[i - 1].append([j - 1, l])
        adj_list_reversed[j - 1].append([i - 1, l])

    preprocessed_graph, preprocessed_graph_reversed, priorities, shortcuts_history = contraction(adj_list, adj_list_reversed)
    print("Ready")

    q = int(input())
    queries = []
    for _ in range(q):
        query = list(map(int, input().split()))
        k = query[0]    # the number of locations that the truck must visit, including the depot
        depot = query[1]
        stores = query[2:]
        queries.append((depot - 1, [x - 1 for x in stores]))

    for start_node, stores in queries:
        dist_matrix, path_matrix = create_distance_matrix([start_node] + stores, preprocessed_graph, preprocessed_graph_reversed, priorities)
        result, memo = held_karp(dist_matrix)

        if result == float("inf"):
            print(-1)
        else:
            print(result if result != float("inf") else -1)
            path = reconstract_path(memo, dist_matrix, path_matrix, result, start_node, stores, shortcuts_history)
        # print(path)



    # depot = 90
    # stores = [10, 27, 32]
    # dist_matrix = [
    #                 [0, 16, 11, 6], 
    #                 [8, 0, 13, 16], 
    #                 [4, 7, 0, 9], 
    #                 [5, 12, 2, 0]
    #             ]
    # result, memo = held_karp(dist_matrix)
    # print(result)   
    # path = reconstract_path(memo, dist_matrix, result, depot, stores)
    # print(path)