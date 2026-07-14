# Given an directed graph with possibly negative edge weights and with 𝑛 vertices and 𝑚 edges as well
# as its vertex 𝑠, compute the length of shortest paths from 𝑠 to all other vertices of the graph.

# Bellman-Ford Algorithm


def bellman_ford_algorithm(n: int, edge_list: list, start_point: int) -> None:

    distance = [float('inf')] * n
    distance[start_point - 1] = 0

    for _ in range(n - 1):
        for u, v, w in edge_list:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w

    for _ in range(n - 1):
        for u, v, w in edge_list:
            if distance[v] > distance[u] + w:
                distance[v] = float('-inf')

    for x in distance:
        if x == float('-inf'):
            print('-')
        elif x == float('inf'):
            print('*')
        else:
            print(x)



if __name__ == "__main__":
    n, m = map(int, input().split(' '))

    edge_list = []
    
    for _ in range(m):
        u, v, w = map(int, input().split(' '))    
        edge_list.append((u - 1, v - 1, w))

    start_point = int(input())
    bellman_ford_algorithm(n, edge_list, start_point)

