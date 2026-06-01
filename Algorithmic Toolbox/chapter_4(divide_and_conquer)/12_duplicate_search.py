import random
from time import perf_counter


def search_duplicates_with_merge_sort(array: list) :
    if len(array) == 1:
        return False, array
 
    middle = (len(array) - 1) // 2
    has_duplicates_left, left = search_duplicates_with_merge_sort(array[:middle+1])
    has_duplicates_right, right = search_duplicates_with_merge_sort(array[middle+1:])

    if has_duplicates_left or has_duplicates_right:
        return True, []

    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        elif right[j] < left[i]:
            merged.append(right[j])
            j += 1
        else:
            return True, []

    merged.extend(left[i:])
    merged.extend(right[j:])

    return False, merged


def search_duplicates_with_set(array: list):
    return len(set(array)) != len(array)


def search_duplicates_with_quick_search(array: list, start: int = 0, end = None):
    if end == None:
        end = len(array) - 1

    if end - start < 1:
        return False

    pivot = array[start]

    left = start + 1
    right = end 

    while left <= right:

        if array[left] == pivot or array[right] == pivot:
            return True
        elif array[left] > pivot: 
            if array[right] < pivot:
                array[left], array[right] = array[right], array[left]
                left += 1
            right -= 1
        else: 
            left += 1

    array[start], array[left-1]  =  array[left-1], array[start]
   
    left_search = search_duplicates_with_quick_search(array, start, left - 2)  
    right_search = search_duplicates_with_quick_search(array, left, end)  

    return left_search or right_search
     

if __name__ == "__main__":

    n = 10 ** 6
    m = 10 ** 5
    while True:
        
        array = [random.randint(1, m) for _ in range(n)]
        array_copy = array.copy()
        array_copy2 = array.copy()
        array_copy3 = array.copy()

        # array = [1, 4, 2, 5, 7, 8, 9, 10, 12, 14, 17, 21, 4]
        # array3 = array.copy()
        # array = [2, 5, 7, 9, 10, 12, 14, 17, 21]

        start = perf_counter()
        has_duplicates_with_set = search_duplicates_with_set(array)
        search_duplicates_set_time = perf_counter() - start
        # print(has_duplicates_with_set)

        start = perf_counter()
        has_duplicates_with_merge, result = search_duplicates_with_merge_sort(array_copy)
        search_duplicates_merge_time = perf_counter() - start
        # print(has_duplicates_with_merge)

    
        start = perf_counter()
        search_duplicates_quick_search = search_duplicates_with_quick_search(array)
        search_duplicates_quick_search_time = perf_counter() - start
        # print(search_duplicates_quick_search)

        print(f"{search_duplicates_set_time} -- {search_duplicates_merge_time} -- {search_duplicates_quick_search_time}")

        if not (has_duplicates_with_merge == has_duplicates_with_set == search_duplicates_quick_search): 
            print(array)
            break