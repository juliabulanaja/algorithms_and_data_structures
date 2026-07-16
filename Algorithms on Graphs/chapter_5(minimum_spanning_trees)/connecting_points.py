# Kruskal algorithm

# The goal is to build roads between some pairs of the
# given cities such that there is a path between any two cities and the
# total length of the roads is minimized.

from queue import PriorityQueue


def calulate_distance(p1: tuple, p2: tuple) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5 


def find_set(point: tuple, sets: list[set]) -> set:
    for set_ in sets:
        if point in set_:
            return set_
    

def kruskal(points: list[tuple]) -> None:

    n = len(points)
    edges = PriorityQueue()

    for i in range(n - 1):
        for j in range(i + 1, n):
            edges.put((calulate_distance(points[i], points[j]), points[i], points[j]))

    sets = [{point} for point in points]
    total_cost = 0
    node_count = 0


    while not edges.empty():
        cost, p1, p2 = edges.get()
        set1 = find_set(p1, sets)
        set2 = find_set(p2, sets)


        if set1 != set2:
            total_cost += cost
            set1.update(set2)
            sets.remove(set2)

            node_count += 1

        if node_count == n:
            break   

    print(f"{total_cost:.7f}")


if __name__ == "__main__":
    n = int(input().strip())
    points = []

    for _ in range(n):
        x, y = map(int, input().split(" ")) 
        points.append((x, y))

    kruskal(points)
