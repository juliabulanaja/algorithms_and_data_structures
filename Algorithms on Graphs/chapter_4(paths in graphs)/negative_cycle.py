# Given an directed graph with possibly negative edge weights and with 𝑛 vertices and 𝑚 edges, check
# whether it contains a cycle of negative weight.


def negative_cycle(n: int, edge_list: list) -> None:

    distance = [float('inf')] * n

    for start_point in range(n):

        if distance[start_point] == float('inf'):

            distance[start_point] = 0
            for _ in range(n - 1):
                for u, v, w in edge_list:
                    if distance[v] > distance[u] + w:
                        distance[v] = distance[u] + w

            for _ in range(n - 1):
                for u, v, w in edge_list:
                    if distance[v] > distance[u] + w:
                        distance[v] = float('-inf')
                        print(1)
                        return
    print(0)


if __name__ == "__main__":
    n, m = map(int, input().split(' '))

    edge_list = []
    
    for _ in range(m):
        u, v, w = map(int, input().split(' '))    
        edge_list.append((u - 1, v - 1, w))

    negative_cycle(n, edge_list)


 

