# Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges, check whether it is bipartite. Output 1 if the graph is bipartite and 0 otherwise.
from collections import deque


def set_color(parent_color):
    if parent_color == 0:
        return 1
    return 0

def bipartite(adj_list):

    colors = [None] * len(adj_list)

    for start_node in range(len(adj_list)):
        if colors[start_node] is not None:
            continue

        q = deque()
        q.append(start_node)
        colors[start_node] = 0

        while q:
            u = q.popleft()
            u_color = colors[u]

            for v in adj_list[u]:
                if colors[v] == None:
                    q.append(v)
                    colors[v] = set_color(u_color)
                elif colors[v] == u_color:
                    return 0
        
    return 1



if __name__ == "__main__":
    n, m = map(int, input().split(' '))

    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split(' '))
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(u - 1)

    # print(adj_list)
    # adj_list = [[3], [4, 3], [3], [1, 2, 0], [1]] # --> 1
    # adj_list = [[1, 3, 2], [0, 2], [1, 0], [0]] # --> 0

    print(bipartite(adj_list))
