def get_left_bound(array: list, q: int) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (right - left) // 2 + left

        if array[middle] < q:
            left = middle + 1
        else: 
            right = middle - 1
    return left

def get_right_bound(array: list, q: int) -> int:
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (right - left) // 2 + left

        if array[middle] > q:
            right = middle - 1
        else: 
            left = middle + 1
    return right

def count_occurrences(array: list, q: int) -> int:

    left_bound = get_left_bound(array, q)
    right_bound = get_right_bound(array, q)

    if left_bound > right_bound:
        return 0
    
    return right_bound - left_bound + 1


if __name__ == "__main__":
    array = [1, 2, 3, 3, 3, 3, 5, 5, 5, 9]
    result = count_occurrences(array, 3)
    print(result)