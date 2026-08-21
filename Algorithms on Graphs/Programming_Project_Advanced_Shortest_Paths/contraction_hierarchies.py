# Task. Compute the distance between several pairs of nodes in the network
import heapq


def witness_path(start_node: int, adj_list: list, node_to_avoid: int = None, contracted: list = None, distance_limit: float = None, node_limit: int = None) -> list:
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
    k = 0

    queue = [(0, start_node)]
    while queue:
        d, current_node = heapq.heappop(queue)

        if d > distances[current_node]:
            continue

        if distance_limit is not None and d > distance_limit:
            break

        k += 1

        if node_limit is not None and k > node_limit:
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


def contraction(initial_graph: list, initial_graph_reversed: list) -> tuple[list, list, list]:
    """Preprocess a graph using the Contraction Hierarchies algorithm.

    Vertices are contracted according to their dynamically calculated
    priorities. When contracting a vertex, necessary shortcut edges are
    added to preserve shortest-path distances. The function also records
    the contraction order of all vertices.

    Args:
        initial_graph: Forward adjacency list representing the original
            directed graph. Each edge is represented as [neighbor, weight].
        initial_graph_reversed: Reversed adjacency list of the original
            graph. Each edge is represented as [predecessor, weight].

    Returns:
        A tuple containing:
            - augmented_graph: Forward adjacency list containing original
              and shortcut edges.
            - augmented_graph_reversed: Reversed adjacency list containing
              original and shortcut edges.
            - final_priorities: List where each element is the contraction
              rank of the corresponding vertex.
            - shortcuts_history: Dictionary recording the contracted vertex
              responsible for each shortcut edge.
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


def calculate_distance(start_node: int, target_node: int, preprocessed_graph: list, preprocessed_graph_reversed: list, priorities: list, shortcuts_history: dict) -> float:
    """Calculate the shortest-path distance using a Contraction Hierarchy.

    Performs a bidirectional Dijkstra search restricted to upward edges,
    meaning edges leading to vertices with a higher contraction rank.

    Args:
        start_node: Source vertex.
        target_node: Destination vertex.
        preprocessed_graph: Forward graph containing original and shortcut
            edges.
        preprocessed_graph_reversed: Reversed graph containing original and
            shortcut edges.
        priorities: Contraction rank assigned to each vertex.
        shortcuts_history: Dictionary containing information about shortcut
            edges. Currently retained for compatibility with path restoration.

    Returns:
        The shortest-path distance from start_node to target_node, or -1
        if the target is unreachable.
    """

    total_nodes = len(priorities)

    distances = [float("inf")] * total_nodes
    distances_reversed = [float("inf")] * total_nodes
    distances[start_node] = 0
    distances_reversed[target_node] = 0

    processed = [False] * total_nodes
    processed_reversed = [False] * total_nodes

    best_distance = float("inf")

    queue = [(0, start_node)]
    queue_reversed = [(0, target_node)]

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
                            heapq.heappush(queue, (distances[neighbor], neighbor))

            if processed_reversed[node] and distances[node] + distances_reversed[node] < best_distance:
                best_distance = distances[node] + distances_reversed[node]

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
                            heapq.heappush(queue_reversed, (distances_reversed[neighbor], neighbor))

            if processed[node_r] and distances_reversed[node_r] + distances[node_r] < best_distance:
                best_distance = distances[node_r] + distances_reversed[node_r]

    return best_distance if best_distance != float("inf") else -1

    

if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    adj_list = [[] for _ in range(n + 1)]
    adj_list_reversed = [[] for _ in range(n + 1)]
    for _ in range(m):
        i, j, l = map(int, input().split(" "))
        adj_list[i - 1].append([j - 1, l])
        adj_list_reversed[j - 1].append([i - 1, l])

    preprocessed_graph, preprocessed_graph_reversed, priorities, shortcuts_history = contraction(adj_list, adj_list_reversed)
    print("Ready")
    # print(preprocessed_graph)
    q = int(input())

    queries = []
    for _ in range(q):
        u, v = map(int, input().split(" "))
        queries.append((u - 1, v - 1))

    for start_node, target_node in queries:
        result = calculate_distance(start_node, target_node, preprocessed_graph, preprocessed_graph_reversed, priorities, shortcuts_history)
        print(result)
