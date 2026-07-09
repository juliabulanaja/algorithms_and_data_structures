from collections import deque


def bfs(start, end, adj_list):
    

    dist = [-1] * len(adj_list)
    dist[start - 1] = 0
    q = deque()
    q.append(start-1)

    while q:
        u = q.popleft()
        for v in adj_list[u]:
            if dist[v] == -1:
                q.append(v)
                dist[v] = dist[u] + 1

    print(dist[end - 1])




if __name__ == "__main__":
    n, m = map(int, input().split(' '))
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u, v = list(map(int, input().split(' ')))
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(u - 1)

    u, v = map(int, input().split(' '))


    bfs(u, v, adj_list)


