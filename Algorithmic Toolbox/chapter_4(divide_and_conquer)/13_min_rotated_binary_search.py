array = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]

def find_min(array: list):

    left = 0
    right = len(array ) - 1
    
    while left < right:
        if array[left] <= array[right]:
            break

        middle = (right + left) // 2

        if array[middle] >= array[left]:
            left = middle + 1
        else: 
            right = middle
    return array[left]


if __name__ == "__main__":
    result = find_min(array)
    print(result)