# Prim's algorithm

# The goal is to build roads between some pairs of the
# given cities such that there is a path between any two cities and the
# total length of the roads is minimized.

import heapq


def calculate_distance(p1: tuple, p2: tuple) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5 


def prim(points: list[tuple[int, int]]) -> None:
    
    visited = set()
    heap = [(0, points[0])]
    total_cost = 0

    while heap:
        distance, current_point = heapq.heappop(heap)
        if current_point in visited:
            continue

        visited.add(current_point)
        total_cost += distance

        for neighbor in points:
            if neighbor in visited:
                continue
            neighbor_distance = calculate_distance(current_point, neighbor)
            heapq.heappush(heap, (neighbor_distance, neighbor))
            

    print(f"{total_cost:.9f}")

if __name__ == "__main__":
    n = int(input().strip())
    points = []

    for _ in range(n):
        x, y = map(int, input().split(" ")) 
        points.append((x, y))

    prim(points)