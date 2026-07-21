# Compute the distance between several pairs of nodes in the network.
import heapq


def bidirectional_dijksrta(adj_list: list[list], adj_list_reversed: list[list], start: int, end: int) -> int:

    if start == end:
        return 0
    start -= 1
    end -= 1

    destinations = [float("inf")] * n
    destinations[start] = 0

    destinations_reversed = [float('inf')] * n
    destinations_reversed[end] = 0

    pq = [(destinations[start], start)]
    pq_reversed = [(destinations_reversed[end], end)]

    processed = [False] * n
    processed_reversed = [False] * n

    best_distance = float("inf")

    while pq and pq_reversed:
        _, uf = heapq.heappop(pq)

        if not processed[uf]:
            processed[uf] = True

            if processed_reversed[uf]:
                break

            for v, w in adj_list[uf]:
                if destinations[v] > destinations[uf] + w:
                    destinations[v] = destinations[uf] + w
                    heapq.heappush(pq, (destinations[v], v))

                    if destinations[v] + destinations_reversed[v] < best_distance:
                        best_distance = destinations[v] + destinations_reversed[v]

        
        _, ub = heapq.heappop(pq_reversed)

        if not processed_reversed[ub]:
            processed_reversed[ub] = True

            if processed[ub]:
                break

            for v, w in adj_list_reversed[ub]:
                if destinations_reversed[v] > destinations_reversed[ub] + w:
                    destinations_reversed[v] = destinations_reversed[ub] + w
                    heapq.heappush(pq_reversed, (destinations_reversed[v], v))

                    if destinations[v] + destinations_reversed[v] < best_distance:
                        best_distance = destinations[v] + destinations_reversed[v]

        

    return best_distance if best_distance != float("inf") else -1


if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    adj_list = [[] for _ in range(n)]
    adj_list_reversed = [[] for _ in range(n)]

    for _ in range(m):
        u, v, l = map(int, input().split(" "))
        adj_list[u - 1].append((v - 1, l))
        adj_list_reversed[v - 1].append((u - 1, l))

    q = int(input())
    queries = []
    for _ in range(q):
        u, v = map(int, input().split(" "))
        queries.append((u, v))

    for u, v in queries:
        result = bidirectional_dijksrta(adj_list, adj_list_reversed, u, v)
        print(result)

