# Clustering with the Kruskal’s algorithm
from queue import PriorityQueue


def calculate_distance(p1: tuple, p2: tuple) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5 


def find_set(point: tuple, sets: list[set]) -> set:
    for set_ in sets:
        if point in set_:
            return set_
    

def clustering(points: list[tuple], k: int) -> float:

    n = len(points)
    edges = PriorityQueue()

    for i in range(n - 1):
        for j in range(i + 1, n):
            edges.put((calculate_distance(points[i], points[j]), i, j))

    sets = [{point} for point in points]

    while not edges.empty():
        current_cost, idx1, idx2 = edges.get()
        p1 = points[idx1]
        p2 = points[idx2]


        set1 = find_set(p1, sets)
        set2 = find_set(p2, sets)

        if len(sets) == k:
            
            if set1 is not set2:
                return current_cost
            continue

        if set1 is not set2:
            set1.update(set2)
            sets.remove(set2)


if __name__ == "__main__":
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split(" "))
        points.append((x, y))

    k = int(input())

    result = clustering(points, k)
    print(f"{result:.12f}")