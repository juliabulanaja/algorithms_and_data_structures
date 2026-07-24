# Compute the distance between several pairs of nodes in the network.
import heapq


def get_heuristics(u: int, v: int, node_coordinates: list[tuple]) -> list[float]:
    x1, y1 = node_coordinates[u]
    x2, y2 = node_coordinates[v]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def a_star_bidirectional(start_node: int, target_node: int, adj_list: list[list], adj_list_reversed: list[list], node_coordinates: list[tuple]) -> int:
    if start_node == target_node:
        return 0

    total_nodes = len(node_coordinates)

    dist_f = [float("inf")] * total_nodes
    dist_r = [float("inf")] * total_nodes

    dist_f[start_node] = 0
    dist_r[target_node] = 0

    processed_f = [False] * total_nodes
    processed_r = [False] * total_nodes

    queue_f = [(get_heuristics(start_node, target_node, node_coordinates), start_node)]
    queue_r = [(get_heuristics(target_node, start_node, node_coordinates), target_node)]

    best_distance = float("inf")

    while queue_f and queue_r:

        if len(queue_f) <= len(queue_r):

            estimated_distance, current_node = heapq.heappop(queue_f)

            if estimated_distance >= best_distance: 
                break

            if not processed_f[current_node]:
                processed_f[current_node] = True

                for neighbor, edge_weight in adj_list[current_node]:
                    if not processed_f[neighbor]:
                        
                        if dist_f[neighbor] > dist_f[current_node] + edge_weight:
                            dist_f[neighbor] = dist_f[current_node] + edge_weight

                            heuristic_to_target = get_heuristics(neighbor, target_node, node_coordinates)
                            estimated_total_distance = heuristic_to_target + dist_f[neighbor]

                            heapq.heappush(queue_f, (estimated_total_distance, neighbor))   

                            if dist_r[neighbor] != float('inf'):
                                total_distance = dist_f[neighbor] + dist_r[neighbor]
                                best_distance = total_distance if total_distance < best_distance else best_distance

        else:

            estimated_distance, current_node = heapq.heappop(queue_r)

            if estimated_distance >= best_distance: 
                break

            if not processed_r[current_node]:
                processed_r[current_node] = True

                for neighbor, edge_weight in adj_list_reversed[current_node]:
                    if not processed_r[neighbor]:

                        if dist_r[neighbor] > dist_r[current_node] + edge_weight:
                            dist_r[neighbor] = dist_r[current_node] + edge_weight

                            heuristic_to_target = get_heuristics(neighbor, start_node, node_coordinates)
                            estimated_total_distance = heuristic_to_target + dist_r[neighbor]

                            heapq.heappush(queue_r, (estimated_total_distance, neighbor))   

                            if dist_f[neighbor] != float('inf'):
                                total_distance = dist_f[neighbor] + dist_r[neighbor]
                                best_distance = total_distance if total_distance < best_distance else best_distance

     
    return best_distance if best_distance != float("inf") else -1


if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    node_coordinates = []
    for _ in range(n):
        x, y = map(int, input().split(" "))
        node_coordinates.append((x, y))

    adj_list = [[] for _ in range(n)]
    adj_list_reversed = [[] for _ in range(n)]
    for _ in range(m):
        i, j, l = map(int, input().split(" "))
        adj_list[i - 1].append((j - 1, l))
        adj_list_reversed[j - 1].append((i - 1, l))


    q = int(input())
    queries = []
    for _ in range(q):
        u, v = map(int, input().split(" "))
        queries.append((u - 1, v - 1))

    for start, end in queries:
        result = a_star_bidirectional(start, end, adj_list, adj_list_reversed, node_coordinates)
        print(result)
