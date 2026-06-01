# Organizing a Lottery
import random
from time import perf_counter


def find_solution(segments: list[tuple], points: list[int]):

    segments = sorted(segments, key=lambda item: item[0]) # O(nlogn)
    result = []

    for point in points:

        left = 0
        right = len(segments) - 1
        right_index = None

        while left <= right:
            middle = (right - left) // 2  + left
            segment_x = segments[middle][0]

            if segment_x > point:
                right = middle - 1
            else: 
                left = middle + 1
                right_index = middle
        
        if right_index == None:
            result.append(0)
            continue

        segments_new = sorted(segments[: right_index + 1], key=lambda item: item[1]) # O(nlogn)

        left = 0
        right = len(segments_new) - 1
        left_index = None

        while left <= right:
            middle = (right - left) // 2  + left
            segment_y = segments_new[middle][1]

            if segment_y > point:
                left_index = middle
                right = middle - 1
            else: 
                left = middle + 1
        
        if left_index == None:
            result.append(0)
            continue

        occurencies = right_index - left_index + 1
        result.append(occurencies)
            
    return result


def find_solution2(segments: list[tuple], points: list[int]):

    starts = sorted(l for l, _ in segments)
    ends = sorted(r for _, r in segments)

    result = []

    for point in points:
        left = 0
        right = len(segments) - 1

        while left <= right:

            middle = (right - left) // 2 + left

            if point >= starts[middle]:
                left = middle + 1
            else:
                right = middle - 1

        right_bound = right + 1
        

        left = 0
        right = len(segments) - 1

        while left <= right:

            middle = (right - left) // 2 + left

            if point <= ends[middle]:
                right = middle - 1
            else:
                left = middle + 1
        left_bound = left
        result.append(right_bound - left_bound)
    
    return result


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


def generate_test_data():
    MAX_N = 50_000
    MAX_M = 50_000
    MIN_VAL = -10**8
    MAX_VAL = 10**8
    # Generate segments
    segments = []
    for _ in range(MAX_N):
        left = random.randint(MIN_VAL, MAX_VAL)
        right = random.randint(MIN_VAL, MAX_VAL)
        if left > right:
            left, right = right, left
        segments.append((left, right))

    # Generate points
    points = [random.randint(MIN_VAL, MAX_VAL) for _ in range(MAX_M)]

    return segments, points

# segments, points = generate_test_data()

# n, m = [int(num) for num in input().split(' ')]

# segments = []
# for s in range(n):
#     segments.append(tuple(int(segment) for segment in input().split(' ')))
# points = [int(point) for point in input().split(' ')]
#################################################


# while True:
#     segments, points = generate_test_data()

#     start = perf_counter()
#     result1 = find_solution2(segments, points)
#     print(f"execution time: {perf_counter() - start}")

#     start = perf_counter()
#     result2 = solve_case(segments, points)
#     print(f"execution time: {perf_counter() - start}")

#     if not result1 == result2:
#         print(segments)
#         print(points)

#         print(f"result 1: {result1}")
#         print(f"result 2: {result2}")

#         break

segments, points = generate_test_data()

start = perf_counter()
result1 = find_solution2(segments, points)
print(f"execution time: {perf_counter() - start}")

start = perf_counter()
result2 = solve_case(segments, points)
print(f"execution time: {perf_counter() - start}")
print(result1 == result2)
