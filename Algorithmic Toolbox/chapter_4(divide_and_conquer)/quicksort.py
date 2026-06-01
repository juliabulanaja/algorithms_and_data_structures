import random 
from time import perf_counter


def quick_sort(array: list, start: int, end: int):

    # print(start, end)

    if end - start < 1:
        return 

    pivot = array[start]
    pivot_first_position = start
    pivot_count = 1

    for i in range(start + 1, end + 1):
        element = array[i]
        if array[i] < pivot:
            if i == pivot_first_position + pivot_count:
                array[pivot_first_position], array[i] = array[i], array[pivot_first_position]
            else:
                array[pivot_first_position], array[pivot_first_position + pivot_count], array[i] = array[i], array[pivot_first_position], array[pivot_first_position + pivot_count]

            pivot_first_position += 1

        elif array[i] == pivot:
            array[pivot_first_position + pivot_count], array[i] = array[i], array[pivot_first_position + pivot_count]
            pivot_count += 1

    quick_sort(array, start, pivot_first_position - 1)     
    quick_sort(array, pivot_first_position + pivot_count, end)    
    

def quick_sort_classic(array: list, start: int = 0, end = None):
    if end == None:
        end = len(array) - 1

    if end - start < 1:
        return 

    pivot = array[start]

    left = start
    right = end 
    left_count = start

    while left < right:
        left += 1

        if array[left] > pivot: 
            
            while left < right:
                if array[right] < pivot:
                    array[left], array[right] = array[right], array[left]
                    left_count += 1
                    right -= 1
                    break
                else: 
                    right -= 1
        else: 
            left_count += 1

    # print('left ', left, 'right ', right, 'left_count ', left_count)  
    array[start], array[left_count]  =  array[left_count], array[start]
   
    quick_sort_classic(array, start, left_count - 1)  
    quick_sort_classic(array, left_count + 1, end)  


def quick_sort_classic2(array: list, start: int = 0, end = None): # the most correct
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
            left += 1

    array[start], array[left-1]  =  array[left-1], array[start]
   
    quick_sort_classic(array, start, left - 2)  
    quick_sort_classic(array, left, end)  




if __name__ == "__main__":

    n = 10 ** 5
    m = 10 ** 5

    while True:
        
        array = [random.randint(1, m) for _ in range(n)]
        array_copy = array.copy()
        array_copy2 = array.copy()

        start = perf_counter()
        sorted_array = sorted(array)
        sorted_array_time = perf_counter() - start

        start = perf_counter()
        quick_sort(array, 0, n-1)
        quick_sort_time = perf_counter() - start

        start = perf_counter()
        quick_sort_classic(array_copy)
        quick_sort_classic_time = perf_counter() - start

        start = perf_counter()
        quick_sort_classic2(array_copy2)
        quick_sort_classic_time2 = perf_counter() - start

        print(f"{sorted_array_time} -- {quick_sort_time} -- {quick_sort_classic_time} -- {quick_sort_classic_time2}")

        if array != sorted_array or array != array_copy or array != array_copy2:   
            print(array)
            break

    # array = [10, 9, 9, 10, 12, 8, 10, 12, 1, 6]
    # array = [10, 9, 9, 10, 12, 18, 10, 12,11, 16]
    # array = [10, 9, 9, 1, 1, 8, 1, 2, 1, 6]
    # array = [10, 11, 3]
    # array = [10, 3, 11]
    # array = [10, 11, 11]
    # array = [10, 3, 3]
    # quick_sort_classic(array, 0, len(array) - 1)
    # print(array)


