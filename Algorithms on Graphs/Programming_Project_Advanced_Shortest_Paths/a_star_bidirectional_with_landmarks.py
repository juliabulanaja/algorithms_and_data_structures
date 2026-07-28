# Compute the distance between several pairs of nodes in the network
import heapq


def dijkstra(start_node: int, adj_list: list) -> list:
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
    for i, neighbors in enumerate(adj_list):
        if neighbors:
            return i
    return None


def preprocessing(adj_list: list, adj_list_reversed: list) -> dict:
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
    closest_landmark = None
    closest_distance = float("inf")
    for l, (graph, _) in preprocessed_graph.items():
        if graph[node] < closest_distance:
            closest_distance = graph[node]
            closest_landmark = l
    return closest_landmark

        
def heuristic_distance(start_node: int, target_node: int, landmark: int, preprocessed_graph: dict) -> int:

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



    
