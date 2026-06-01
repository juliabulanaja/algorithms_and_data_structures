import random
from bisect import bisect_left
import time


def match_mice(mice: list, holes: list) -> int:

    mice.sort() # O(nlogn)
    holes.sort() # O(nlogn)

    return max([abs(a-b) for a, b in zip(mice, holes)]) # O(n)


def match_mice_with_binary(mice: list, holes: list) -> int:

    holes.sort() # O(nlogn)
    max_distance_for_mice = 0

    print(holes)
    print(mice)


    for mouse in mice:
        
        index = bisect_left(holes, mouse)

        if index < len(holes):
            min_distance_for_mouse = abs(holes[index] - mouse)
        else: 
            min_distance_for_mouse = abs(holes[index-1] - mouse)

        if min_distance_for_mouse > max_distance_for_mice:
            max_distance_for_mice = min_distance_for_mouse

    return max_distance_for_mice



n = 10 ** 1
m = 5
mice = random.sample(range(1, n), m)
holes = random.sample(range(1, n), m)


result1 = match_mice(mice, holes)
print(result1)

print("______________________")

result2 = match_mice_with_binary(mice, holes)
print(result2)
