# Task. Given an directed graph with positive edge weights and with 𝑛 vertices and 𝑚 edges as well as two
# vertices 𝑢 and 𝑣, compute the weight of a shortest path between 𝑢 and 𝑣 (that is, the minimum total
# weight of a path from 𝑢 to 𝑣).
from queue import PriorityQueue


def dijkstra(start, end, adj_list):
    n = len(adj_list)
    start -= 1
    end -= 1

    cost = [float('inf')] * n
    cost[start] = 0

    pq = PriorityQueue()
    pq.put((cost[start], start))

    while not pq.empty():
        c, u = pq.get()

        if u == end:
            break

        for v, w in adj_list[u]:
            if cost[v] > cost[u] + w:
                cost[v] = cost[u] + w
                pq.put((cost[v], v))
    return cost[end] if cost[end] < float('inf') else -1


if __name__ == "__main__":
    n, m = map(int, input().split(' '))

    adj_list = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, w = map(int, input().split(' '))    
        adj_list[u - 1].append((v - 1, w))

    start, end = map(int, input().split(' '))

    result = dijkstra(start, end, adj_list)
    print(result)