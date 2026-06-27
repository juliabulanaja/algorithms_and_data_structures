from collections import deque


def check_connection(adj_list, n):
    visited = [False] * (n + 1)
    clock = 0

    for node, neighbors in enumerate(adj_list):
        if not visited[node] and node > 0:

            visited[node] = True
            clock += 1
            stack = [node]

            while len(stack) > 0:
                current = stack.pop()
                visited[current] = True

                for neighbor in adj_list[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    return clock






if __name__ == "__main__":
    n, m = list(map(int, input().split(' ')))
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        v1, v2 = list(map(int, input().split(' ')))
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    result =  check_connection(adj_list, n)
    print(result)
