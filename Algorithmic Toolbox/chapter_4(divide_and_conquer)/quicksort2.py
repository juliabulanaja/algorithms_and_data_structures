import random 
from time import perf_counter


def quick_sort_classic2(array: list, start: int = 0, end = None):
    if end == None:
        end = len(array) - 1

    if end - start < 1:
        return 

    pivot = array[start]

    left = start + 1
    right = end 

    while left <= right:
        
        if array[left] > pivot: 
            if array[right] < pivot:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
            else:
                right -= 1
        else: 
            left += 1

    array[start], array[left-1]  =  array[left-1], array[start]
   
    quick_sort_classic(array, start, left - 2)  
    quick_sort_classic(array, left, end)  




if __name__ == "__main__":


    array = [10, 9, 9, 10, 12, 8, 10, 12, 1, 6]
    # array = [10, 9, 9, 10, 12, 18, 10, 12,11, 16]
    # array = [10, 9, 9, 1, 1, 8, 1, 2, 1, 6]
    array = [10, 11, 3]
    array = [10, 3, 11]
    array = [10, 11, 11]
    array = [10, 3, 3]
    quick_sort_classic(array, 0, len(array) - 1)
    print(array)


