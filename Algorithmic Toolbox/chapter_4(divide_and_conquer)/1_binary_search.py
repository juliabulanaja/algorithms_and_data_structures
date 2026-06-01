import math


n = int(input())
array = [int(num) for num in input().split(' ')]

m = int(input())
array_m = [int(num) for num in input().split(' ')]
# array = [1, 2, 4, 5, 6, 10, 12, 13, 15, 16, 20]

def binary_search(array: list, q: int) -> int:
    left = 0
    right = len(array) - 1
    
    while left <= right:
        middle = math.ceil((right - left) / 2) + left
        if q == array[middle]:
            return str(middle)
        elif q > array[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return '-1'


        
result = ' '.join([binary_search(array, i) for i in array_m])
print(result)