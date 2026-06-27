from collections import deque


def check_path(start, target, n, adj_list):
    visited = [False] * (n + 1)
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        current = queue.popleft()
        if current == target:
            return 1

        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return 0


if __name__ == "__main__":
    n, m = list(map(int, input().split(' ')))
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        v1, v2 = list(map(int, input().split(' ')))
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    start, target = list(map(int, input().split(' ')))
    
    # n = 4
    # adj_list = [[], [2, 4], [1, 3], [2, 4], [3, 1]]
    # start, target = 1, 4

    result = check_path(start, target, n, adj_list)
    print(result)

