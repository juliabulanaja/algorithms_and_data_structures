import random


def find_smallest_missing_element(array: list):    
    left = 0
    right = len(array) - 1

    while left <= right:

        if (right - left) == array[right] - array[left]:
            return -1
                
        middle = (right - left) // 2 + left

        if (middle - left) < array[middle] - array[left]:
            right = middle
        elif (right - middle - 1) < array[right] - array[middle + 1]:
            left = middle
        else:
            return array[middle] + 1

        
if __name__ == "__main__":

    while True:
        n = 20
        m = 50
        array = [random.randint(1, m) for _ in range(n)]
        array.sort()

        # array = [1, 2, 3, 5, 8, 10, 12]
        # array = [2, 5, 7, 9, 9, 10, 12, 14, 17, 21]
        # array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        result = find_smallest_missing_element(array)
        print(array)
        print(result)