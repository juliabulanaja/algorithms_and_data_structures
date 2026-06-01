import math
n = int(input())
array = [int(num) for num in input().split(' ')]

m = int(input())
array_m = [int(num) for num in input().split(' ')]


# array = [2, 2, 2, 3, 4, 7, 8, 8, 10, 10, 11, 11, 12, 12, 15, 15, 15, 15, 17, 18, 18]

def binary_search_duplicates(array: list, q: int):
    left = 0
    right = len(array) - 1
    index = -1

    while left <= right:
        middle = math.ceil((right - left) / 2) + left

        if array[middle] == q:
            index = middle
        if array[middle] >= q:
            right = middle - 1
        else:
            left = middle + 1
    
    return str(index)


      
result = ' '.join([binary_search_duplicates(array, i) for i in array_m])
print(result)

