# n = int(input())

# segments = []

# for _ in range(n):
#     a, b = [int(num) for num in input().split(' ')]
#     segments.append((a, b))

import random

def covering_segments(segments: list[tuple]) -> list[int]:
    segments = sorted(segments, key=lambda o: o[0])
    result = []
    previous = segments[0]
    for i in range(1, len(segments)): 
        current = segments[i] 
        if previous[1] >= current[0]:
            previous = (current[0], min(previous[1], current[1]))
        else:
            result.append(previous[1]) 
            previous = current 
    result.append(previous[1]) 
    return result

def covering_segments_2(segments):
    sorted_segments = sorted(segments, key=lambda o: o[1])
    previous_cut = -1
    answer = []
    for segment in sorted_segments:
        if segment[0] > previous_cut:
            previous_cut = segment[1]
            answer.append(previous_cut)
    return answer

# result = covering_segments(segments)
# print(len(result))
# print(*result)

# segments = [(1, 4), (2, 3), (3, 6), (4, 8)]
segments = []
for segment_id in range(random.randint(10, 100)):
    start = random.randint(1, (10 ** 9) - 1)
    end = random.randint(start, 10 ** 9)
    segments.append((start, end))
from time import perf_counter

s = perf_counter()
result = covering_segments(segments)
print(perf_counter() - s)
s = perf_counter()
result_2 = covering_segments_2(segments)
print(perf_counter() - s)
print(len(result))
print(len(result_2))

