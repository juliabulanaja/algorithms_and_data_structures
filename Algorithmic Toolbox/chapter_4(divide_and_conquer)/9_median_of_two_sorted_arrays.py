from statistics import median
from time import perf_counter
import random
import heapq
import time


def get_median_linear(array_a: list, array_b: list):
    a = 0
    b = 0

    lenght = len(array_a) 
    prev = 0
    curr = 0

    for _ in range(lenght + 1):
        prev = curr

        if b >= lenght or (a < lenght and array_a[a] <= array_b[b]) :
            curr = array_a[a]
            a += 1
        elif a >= lenght or (b < lenght and array_a[a] > array_b[b]):
            curr = array_b[b]
            b += 1    

    return (prev + curr) / 2

def median_two_sorted_arrays_bruteforce(array_a: list, array_b: list):
    aa = a.copy()
    aa.extend(b)
    aa.sort()
    return median(aa)


def get_median_with_binary_search(array1: list, array2: list):
    n = len(array1)

    low = 0
    high = n - 1

    r1 = high // 2 
    r2 = n - r1 - 2

    while True:

        left1 = array1[r1] if r1 >= 0 else -float('inf')
        right1 = array1[r1 + 1] if (r1 + 1) < n else float('inf')

        left2= array2[r2] if r2 >= 0 else -float('inf')
        right2  = array2[r2 + 1] if (r2 + 1) < n else float('inf')

        if left1 > right2:
            high = r1 - 1
            r1 = (high + low) // 2
            r2 = n - r1 - 2

        if  left2 > right1:
            low = r1 + 1
            r1 = (high + low) // 2
            r2 = n - r1 - 2

        if left1 <= right2 and left2 <= right1:
            return (max(left1, left2) + min(right1, right2)) / 2


if __name__ == "__main__":
    
    while True:
        n = 10**7
        m = 10**5
        a = [random.randint(1, m) for _ in range(n)]
        b = [random.randint(1, m) for _ in range(n)]
        a.sort()
        b.sort()

        print("______________________________")
        start = perf_counter()
        median2 = get_median_linear(a, b)
        print(f"Merge Sort execution time is: {perf_counter() - start}. Median: {median2}")

        start = perf_counter()
        median3 = get_median_with_binary_search(a, b)
        print(f"Binary serch execution time is: {perf_counter() - start}. Median: {median3}")

        start = perf_counter()
        median1 = median_two_sorted_arrays_bruteforce(a, b)
        print(f"Naive execution time is: {perf_counter() - start}. Median: {median1}")

        if median1 != median2 or median1 != median3:
            print(median1, median2, median3)
            print(a)
            print(b)
            break
        # break