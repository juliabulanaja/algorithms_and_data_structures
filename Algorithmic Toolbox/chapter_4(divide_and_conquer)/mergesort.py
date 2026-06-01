import random 
from time import perf_counter


def merge_sort(array: list):
    if len(array) < 2:
        return array

    middle_index = (len(array) - 1) // 2 

    array_b = merge_sort(array[:middle_index + 1])
    array_c = merge_sort(array[middle_index + 1:])

    array_a = []
    b = 0
    c = 0
    for i in range(len(array_b) + len(array_c)):

        if b >= len(array_b):
            array_a.extend(array_c[c:])
            break
        if c >= len(array_c):
            array_a.extend(array_b[b:])
            break
        
        if array_b[b] <= array_c[c]:
            array_a.append(array_b[b])
            b += 1
        else: 
            array_a.append(array_c[c])
            c += 1

    return array_a

def merge_sort_gen(arr, left, right):
    if right - left < 1:
        yield arr[left]
        return

    middle_index = (left + right) // 2
    left_half = merge_sort_gen(arr, left, middle_index)
    right_half = merge_sort_gen(arr, middle_index + 1, right)

    left_value = next(left_half, None)
    right_value = next(right_half, None)

    while left_value is not None and right_value is not None:
        if left_value < right_value:
            yield left_value
            left_value = next(left_half, None)
        else:
            yield right_value
            right_value = next(right_half, None)
    if left_value is not None:
        yield left_value
        yield from left_half
    elif right_value is not None:
        yield right_value
        yield from right_half



array = [random.randint(1, 10**9) for _ in range(10**5)]

start = perf_counter()
result = merge_sort(array)
print(f"time: {perf_counter() - start}")

start = perf_counter()
result2 = list(merge_sort_gen(array, 0, len(array) - 1))
print(f"time: {perf_counter() - start}")

print(result == result2)