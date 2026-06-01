from functools import cmp_to_key

n = int(input())
numbers = [int(num) for num in input().split(' ')]

def custom_sort(a: int, b: int) -> int:
    if int(str(a) + str(b)) > int(str(b) + str(a)):
        return -1
    return 1

def find_largest_number(numbers: list) -> int:
    sorted_numbers = sorted(numbers, key=cmp_to_key(custom_sort))
    return int("".join(map(str, sorted_numbers)))

# numbers = [21, 2]
# numbers = [9, 4, 6, 1, 9]
# numbers = [23, 39, 92]
result = find_largest_number(numbers)
print(result)