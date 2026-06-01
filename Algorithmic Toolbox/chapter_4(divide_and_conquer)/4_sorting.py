# Improving QuickSort
import random


# array = [2, 3, 9, 2, 2]
# array = [6, 9, 9, 3, 9, 8, 9, 4, 7, 6, 1]
# array = [6, 8, 9, 5, 5, 3, 9, 8, 9, 6, 4, 7, 6, 1, 5]
# array = [6, 8, 9, 3, 9, 8, 9, 6, 4, 7, 6, 1, 5]

def sort(array: list, start: int, end: int) -> list:

    if end - start <= 1:
        return 

    pivot = array[random.randint(start, end - 1)]

    pivot_boundary = start # < pivot
    pivot_count = 0 # = pivot

    for k in range(start, end):

        if array[k] == pivot:
            array[pivot_boundary + pivot_count], array[k] = array[k], array[pivot_boundary + pivot_count]
            pivot_count += 1

        elif array[k] < pivot:   
            if k == pivot_boundary + pivot_count or pivot_count == 0:
               array[pivot_boundary], array[k] = array[k], array[pivot_boundary]
            else:
                array[pivot_boundary], array[pivot_boundary + pivot_count], array[k] = array[k], array[pivot_boundary], array[pivot_boundary + pivot_count]

            pivot_boundary += 1
    
    sort(array, start, pivot_boundary)
    sort(array, pivot_boundary + pivot_count, end)

def sort2(array: list, start: int, end: int) -> list:

    if end - start < 1:
        return 

    pivot = array[random.randint(start, end)]

    lt = start
    pc = 0

    for i in range(start, end+1):

        if array[i] == pivot:
            array[lt + pc], array[i] = array[i], array[lt + pc]
            pc += 1

        if array[i] < pivot:
            array[lt + pc], array[i] = array[i], array[lt + pc]
            
            if pc > 0:
                array[lt],  array[lt + pc] = array[lt + pc], array[lt]
            lt += 1

    sort2(array, start, lt - 1)
    sort2(array, lt + pc, end)


n = int(input())
array = [int(num) for num in input().split(' ')]

sort2(array, 0, len(array)-1)
print(' '.join([str(i) for i in array]))