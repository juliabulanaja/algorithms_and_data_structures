# Compute the distance between several pairs of nodes in the network.
import heapq


def precompute_heuristics(target_node: int, nodes: list[tuple]) -> list[float]:
    target_x, target_y = nodes[target_node]
    
    heuristic_distances = []
    for x, y in nodes:
        distance = ((target_x - x)**2 + (target_y - y)**2)**0.5
        heuristic_distances.append(distance)
        
    return heuristic_distances


def a_star(start_node: int, end_node: int, adj_list: list(tuple), nodes: list) -> int:
    total_nodes = len(adj_list)

    shortest_distances = [float("inf") for _ in range(total_nodes)]
    shortest_distances[start_node] = 0

    x_end, y_end = nodes[end_node]
    heuristic_distances = precompute_heuristics(end_node, nodes)

    queue = [(heuristic_distances[start_node], start_node)]
    processed = [False] * total_nodes

    while queue:
        estimated_distance, current_node = heapq.heappop(queue)

        if current_node == end_node:
            return shortest_distances[end_node]

        if processed[current_node]:
            continue
        processed[current_node] = True

        for neighbor, edge_weight in adj_list[current_node]:
            if processed[neighbor]:
                continue

            if shortest_distances[neighbor] > shortest_distances[current_node] + edge_weight:
                shortest_distances[neighbor] = shortest_distances[current_node] + edge_weight

                heuristic_to_target = heuristic_distances[neighbor]
                estimated_total_distance = heuristic_to_target + shortest_distances[neighbor]

                heapq.heappush(queue, (estimated_total_distance, neighbor))   

    return -1



if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    nodes = []
    for _ in range(n):
        x, y = map(int, input().split(" "))
        nodes.append((x, y))

    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        i, j, l = map(int, input().split(" "))
        adj_list[i - 1].append((j - 1, l))


    q = int(input())
    queries = []
    for _ in range(q):
        u, v = map(int, input().split(" "))
        queries.append((u - 1, v - 1))

    for start, end in queries:
        result = a_star(start, end, adj_list, nodes)
        print(result)