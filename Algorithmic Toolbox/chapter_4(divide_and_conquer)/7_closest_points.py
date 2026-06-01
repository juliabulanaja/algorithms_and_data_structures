def find_min_distance(points: list):

    if len(points) == 1:
        return float('inf')
    if len(points) == 2:
        return calculate_distance(points[0], points[1])
    if len(points) == 3:
        return max(calculate_distance(points[0], points[1]), 
                    calculate_distance(points[0], points[2]), 
                    calculate_distance(points[1], points[2]))


    points = sorted(points, key=lambda x: x[0])

    middle = len(points) // 2
    d1 = find_min_distance(points[:middle])
    d2 = find_min_distance(points[middle:])
    d = min(d1, d2)

    middle_line = (points[middle-1][0] + points[middle][0]) / 2
    strip_points = sorted([p for p in points if abs(p[0] - middle_line) < d], key=lambda x: x[1])
    
    for i in range(len(strip_points)):
        for j in range(i + 1, len(strip_points)):
            if strip_points[j][1] - strip_points[i][1] >= d:
                break
            d = min(d, calculate_distance([strip_points[j], strip_points[i]]))
    return d


def calculate_distance(p1, p2) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


if __name__ == "__main__":

    n = int(input())

    points = []
    for s in range(n):
        points.append(tuple(int(point) for point in input().split(' ')))


    result = find_min_distance(points)
    print(f"{result:.9f}")
