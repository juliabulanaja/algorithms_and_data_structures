
def dfs(value):

    states[value] = True   
    for c in adj_list[value]:
        if not states[c]:
            dfs(c)
    order.append(value + 1)


def toposort(n, adj_list):
    
    for i in range(n):
        if not states[i]:
            dfs(i)
    order.reverse()
    print(' '.join(map(str, order)))

            
if __name__ == "__main__":
    n, m = list(map(int, input().split(' ')))
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split(' '))
        adj_list[u - 1].append(v - 1)
   
    states = [False] * n
    order = []
    toposort(n, adj_list)

 