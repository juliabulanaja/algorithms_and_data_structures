import sys
sys.setrecursionlimit(5000)


def dfs(value, states, adj_list, order):
    states[value] = True
    for i in adj_list[value]:
        if not states[i]:
            dfs(i, states, adj_list, order)
    order.append(value)


def dfs_postorder(array, adj_list):

    states = [False] * n
    order = []
    for i in array:
        if not states[i]:
            dfs(i, states, adj_list, order)

    order.reverse()
    return order


def find_clusters(array, adj_list):

    states = [False] * n
    order = []
    cluster = 0
    for i in array:
        if not states[i]:
            cluster += 1
            dfs(i, states, adj_list, order)

    return cluster
        

if __name__ == "__main__":
    n, m = list(map(int, input().split(' ')))
    adj_list = [[] for _ in range(n)]
    reversed_adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split(' '))
        adj_list[u - 1].append(v - 1)
        reversed_adj_list[v - 1].append(u - 1)

    postorder = dfs_postorder(range(n), reversed_adj_list)
    cluster_n = find_clusters(postorder, adj_list)
    print(cluster_n)

