# Compute the distance between several pairs of nodes in the network
import heapq


def dijkstra(start_node: int, adj_list: list) -> list:
    """Computes the shortest-path distances from a source node to all reachable nodes.

    Executes Dijkstra's algorithm using a min-heap priority queue to compute non-negative
    shortest path weights from a single source across the given graph.

    Args:
        start_node: The 0-based index of the starting node.
        adj_list: Adjacency list representing the graph, where adj_list[u] is a list 
            of (neighbor, cost) tuples for node u.

    Returns:
        list[float]: A list where the value at index i represents the shortest distance 
        from start_node to node i. Unreachable nodes have a value of float('inf').
    """

    total_nodes = len(adj_list)
    distances = [float('inf')] * total_nodes
    distances[start_node] = 0

    queue = [(0, start_node)]

    while queue:
        d, current_node = heapq.heappop(queue)
        if d > distances[current_node]:
            continue
        for neighbor, cost in adj_list[current_node]:
            if distances[current_node] + cost < distances[neighbor]:
                distances[neighbor] = distances[current_node] + cost
                heapq.heappush(queue, (distances[neighbor], neighbor))

    return distances


def get_start_node(adj_list: list) -> int:
    """Finds the index of the first node in the graph that has at least one outgoing edge.

    Args:
        adj_list: Adjacency list representing the graph, where adj_list[u] is a list 
            of (neighbor, weight) tuples for node u.

    Returns:
        int | None: The 0-based index of the first non-isolated node with outgoing edges, 
        or None if all nodes in the adjacency list have no outgoing edges.
    """
    
    for i, neighbors in enumerate(adj_list):
        if neighbors:
            return i
    return None


def preprocessing(adj_list: list, adj_list_reversed: list) -> dict:
    """Precomputes shortest-path distances to and from greedily chosen landmark nodes.

    Selects landmarks across the graph using a farthest-first strategy. For each
    chosen landmark, Dijkstra's algorithm is run on both the forward and reversed
    graphs to precalculate distances for use as heuristics in Landmark-based A* (ALT).

    Args:
        adj_list: Adjacency list representing the forward graph, where adj_list[u]
            is a list of (neighbor, weight) tuples.
        adj_list_reversed: Adjacency list representing the reversed graph, where
            adj_list_reversed[u] is a list of (predecessor, weight) tuples.

    Returns:
        dict: A dictionary mapping each landmark node index (int) to a tuple of
        two lists:
            - dist_from_landmark (list[float]): Shortest distances from the landmark
              to all nodes in the graph.
            - dist_to_landmark (list[float]): Shortest distances from all nodes in
              the graph to the landmark.
        Returns an empty dictionary if no valid start landmark is found.
    """

    total_nodes = len(adj_list)
    total_landmarks = total_nodes // 1000 or 1
    landmarks = []

    next_landmark = get_start_node(adj_list)
    if next_landmark == None:
        return {}

    global_distances = [float('inf')] * total_nodes
    preprocessed = dict()

    while next_landmark is not None and len(landmarks) < total_landmarks:
        landmarks.append(next_landmark)
        local_distances = dijkstra(next_landmark, adj_list)
        local_distances_reversed = dijkstra(next_landmark, adj_list_reversed)
        preprocessed[next_landmark] = (local_distances, local_distances_reversed)

        next_landmark = None
        max_distance_found = -1

        for i in range(total_nodes):

            if local_distances[i] < global_distances[i]:
                global_distances[i] = local_distances[i]

            if global_distances[i] != float('inf') and global_distances[i] > 0 and max_distance_found < global_distances[i]:
                max_distance_found = global_distances[i]
                next_landmark = i

    return preprocessed


def a_start_with_preprocessing(start_node: int, target_node: int, preprocessed_graph: dict):
    """Computes the shortest path distance between two nodes using Landmark-based A* (ALT).

    Uses precomputed landmark distances as a lower-bound heuristic (via the triangle 
    inequality) to guide A* search towards the target node.

    Args:
        start_node: The 0-based index of the starting node.
        target_node: The 0-based index of the destination node.
        preprocessed_graph: Dictionary mapping landmark indices to a tuple of distance 
            lists: `(dist_from_landmark, dist_to_landmark)`.

    Returns:
        float: The shortest path distance from start_node to target_node, or -1 
        if target_node is unreachable.
    """

    total_nodes = len(adj_list)
    processed = [False] * total_nodes
    shortest_distances = [float("inf")] * total_nodes
    shortest_distances[start_node] = 0

    queue = [(0, start_node)]
    landmark = determine_landmark(start_node, preprocessed_graph)

    while queue:
        distance, current_node = heapq.heappop(queue)
        if current_node == target_node:
            return shortest_distances[target_node]

        if processed[current_node]:
            continue
        processed[current_node] = True

        for neighbor, edge_weight in adj_list[current_node]:
            if processed[neighbor]:
                continue

            if shortest_distances[neighbor] > shortest_distances[current_node] + edge_weight:
                shortest_distances[neighbor] = shortest_distances[current_node] + edge_weight

                heuristic_to_target = heuristic_distance(neighbor, target_node, landmark, preprocessed_graph)
                estimated_total_distance = heuristic_to_target + shortest_distances[neighbor]

                heapq.heappush(queue, (estimated_total_distance, neighbor))  

    return -1


def determine_landmark(node: int, preprocessed_graph: dict) -> int:
    """Selects the preprocessed landmark closest to the given node.

    Iterates through all available landmarks in the preprocessed graph data 
    and returns the one with the smallest precomputed distance from the node.

    Args:
        node: The 0-based index of the node to find a landmark for.
        preprocessed_graph: Dictionary mapping landmark indices to a tuple of distance 
            lists: `(dist_from_landmark, dist_to_landmark)`.

    Returns:
        int | None: The index of the landmark node closest to the input node, or 
        None if no landmarks are available in preprocessed_graph.
    """

    closest_landmark = None
    closest_distance = float("inf")
    for l, (graph, _) in preprocessed_graph.items():
        if graph[node] < closest_distance:
            closest_distance = graph[node]
            closest_landmark = l
    return closest_landmark

        
def heuristic_distance(start_node: int, target_node: int, landmark: int, preprocessed_graph: dict) -> float:
    """Estimates the shortest path distance between start_node and target_node using landmark heuristics.

    Applies the triangle inequality theorem using precomputed landmark distances to calculate
    an admissible lower-bound distance heuristic for A* search.

    Args:
        start_node: The 0-based index of the current node being evaluated.
        target_node: The 0-based index of the destination node.
        landmark: The 0-based index of the chosen landmark node.
        preprocessed_graph: Dictionary mapping landmark indices to a tuple of distance 
            lists: `(dist_from_landmark, dist_to_landmark)`.

    Returns:
        float: The estimated minimum distance between start_node and target_node, or -1 
        if landmark is None.
    """

    if landmark is not None:
        landmark_to_start = preprocessed_graph[landmark][0][start_node]
        landmark_to_target = preprocessed_graph[landmark][0][target_node]
        start_to_landmark = preprocessed_graph[landmark][1][start_node]
        target_to_landmark = preprocessed_graph[landmark][1][target_node]

        return max(landmark_to_target - landmark_to_start, start_to_landmark - target_to_landmark)

    return -1



if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    adj_list = [[] for _ in range(n + 1)]
    adj_list_reversed = [[] for _ in range(n + 1)]
    for _ in range(m):
        i, j, l = map(int, input().split(" "))
        adj_list[i - 1].append((j - 1, l))
        adj_list_reversed[j - 1].append((i - 1, l))

    preprocessed_graph = preprocessing(adj_list, adj_list_reversed)
    print("Ready")

    q = int(input())

    queries = []
    for _ in range(q):
        u, v = map(int, input().split(" "))
        queries.append((u - 1, v - 1))

    for start_node, target_node in queries:
        result = a_start_with_preprocessing(start_node, target_node, preprocessed_graph)
        print(result)



    
