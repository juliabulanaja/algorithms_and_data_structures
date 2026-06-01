import random
from time import perf_counter



def find_range_sum(numbers: list[int], ranges: list[tuple]) -> list[int]:
    result = []
    for start, end in ranges:
        result.append(sum(numbers[start: end+1]))
     
    return result

def find_range_sum_with_prefix_sums(numbers: list[int], ranges: list[tuple]) -> list[int]:
    prefix_sums = [0] * (len(numbers) + 1)
    for i in range(1, len(numbers) + 1):
        prefix_sums[i] = prefix_sums[i - 1] + numbers[i - 1]
    
    result = []
    for start, end in ranges:
        range_sum = prefix_sums[end + 1] - prefix_sums[start]
        result.append(range_sum)
    
    return result


n = 10 ** 8
numbers = [random.randint(-10, 10) for _ in range(n)]
ranges = []
for _ in range(100):
    start = random.randint(0, n-1)
    end = random.randint(start, n-1)
    ranges.append((start, end))



start = perf_counter()
result = find_range_sum(numbers, ranges)
print(f"Function with sorting finished in {(perf_counter() - start):.4f} s.")

start = perf_counter()
result2 = find_range_sum_with_prefix_sums(numbers, ranges)
print(f"Function with sorting finished in {(perf_counter() - start):.4f} s.")

print(result == result2)


