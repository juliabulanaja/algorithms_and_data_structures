def solve_case(segments, points):
    events = []
    for start, end in segments:
        events.append((start, 0))
        events.append((end, 2))
    for point in points:
        events.append((point, 1))
    events.sort()
    result = {}
    active_segments = 0
    for event in events:
        if event[1] == 0:
            active_segments += 1
        elif event[1] == 2:
            active_segments -= 1
        else:
            result[event[0]] = active_segments
    return [result[point] for point in points]


if __name__ == "__main__":

    n, m = [int(num) for num in input().split(' ')]

    segments = []
    for s in range(n):
        segments.append(tuple(int(segment) for segment in input().split(' ')))
    points = [int(point) for point in input().split(' ')]


    result = solve_case(segments, points)
    print(' '.join([str(i) for i in result]))