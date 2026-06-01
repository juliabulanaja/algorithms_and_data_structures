from statistics import median
from time import perf_counter
import random
import time
import heapq


def get_median_with_binary_search(array1: list, array2: list):

    lenght = len(array1) + 1

    r1 = lenght // 2 - 1
    r2 = lenght - r1 - 2
    shift = r1 

    prev1, prev2 = r1, r2

    while True:
        if array2[r2] > array1[r1]:
            shift = max(1, r2 // 2 )
            r1 += shift 
            r2 -= shift
        else:
            shift = max(1, r1 // 2 )
            r1 -= shift 
            r2 += shift

        if shift == 1 and max(array1[r1], array2[r2]) > max(array1[prev1], array2[prev2]):

            combined = array1[max(0, prev1-1) : prev1+1] + array2[max(0, prev2-1) : prev2+1]
            max1, max2 = heapq.nlargest(2, combined)

            return (max1 + max2) / 2

        prev1, prev2 = r1, r2
        


if __name__ == "__main__":
    a = [1, 2, 3, 3, 3, 3, 5, 5, 5, 9]  
    b = [4, 6, 6, 7, 9, 10, 10, 12, 12, 12]

    median3 = get_median(a, b)
    print(median3)

    a = [1, 2, 3, 3, 3, 9, 9, 9, 9, 9]  
    b = [6, 6, 6, 6, 6, 6, 10, 12, 12, 12]

    median3 = get_median(a, b)
    print(median3)

    a = [1, 2, 3, 3, 3, 3, 5, 5, 5, 9]  
    b = [4, 6, 6, 7, 9, 10, 10, 12, 12, 12]

    a = [1, 1, 1, 2, 2, 3, 4, 4, 7, 7] 
    b = [2, 2, 4, 6, 6, 7, 8, 8, 9, 9]

    a = [1, 2, 2, 5, 6, 6, 7, 7, 8, 9] 
    b = [1, 2, 3, 3, 4, 4, 4, 7, 9, 9]

    a = [1, 1, 3, 3, 6, 7, 8, 9, 10, 10]
    b = [2, 3, 3, 3, 5, 5, 6, 7, 8, 9]

    a = [2, 2, 2, 2, 4, 6, 6, 8, 9, 10] 
    b = [1, 2, 3, 3, 5, 5, 5, 5, 9, 9]

    a = [1, 2, 4, 5, 7, 9, 9, 9, 9, 10]
    b = [2, 2, 4, 5, 5, 6, 7, 7, 10, 10]

    a = [1, 1, 5, 5, 7, 8, 8, 9, 9, 10]
    b = [2, 2, 3, 4, 5, 5, 7, 8, 9, 10]

    a = [1, 1, 1, 2, 4, 4, 4, 5, 6, 6] 
    b = [2, 7, 7, 8, 8, 9, 9, 9, 9, 10]

    a = [6, 8, 8, 8, 8, 8, 9, 10, 10, 10] #  median2 
    b = [1, 1, 2, 2, 2, 3, 3, 5, 6, 6]

    a = [1, 1, 1, 2, 2, 2, 2, 4, 4, 5] # median 3
    b = [2, 5, 5, 5, 6, 7, 8, 8, 8, 10]

    a = [5, 7, 7, 7, 7, 7, 9, 9, 10, 10]
    b = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]

    # a = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]
    # b = [5, 7, 7, 7, 7, 7, 9, 9, 10, 10]