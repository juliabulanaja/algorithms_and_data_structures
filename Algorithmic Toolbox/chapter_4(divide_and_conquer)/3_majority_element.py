import math


def majority_element(array: list):
    array.sort()

    middle_index = len(array) // 2
    element = array[middle_index]
    minimum_occurences = len(array) // 2 + 1

    left = 0
    right = middle_index

    while left <= right:
        middle = math.ceil((right - left) / 2) + left
        if array[middle] == element:
            right = middle - 1
            
        else:
            left = middle + 1

    target_index = left + minimum_occurences - 1

    if target_index >= len(array):
        return 0
    target_element = array[target_index]

    return int(element == target_element)


n = int(input())
array = [int(num) for num in input().split(' ')]


result = majority_element(array)
print(result)