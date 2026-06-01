def find_inversions(array: list):

    if len(array) < 2:
        return 0, array

    middle_index = len(array) // 2 

    inversion_number_right, array_right = find_inversions(array[:middle_index])
    inversion_number_left, array_left = find_inversions(array[middle_index:])

    sorted_array = []
    ri = 0
    li = 0
    inversion_number = inversion_number_right + inversion_number_left

    for i in range(len(array_right) + len(array_left)):

        if ri >= len(array_right):
            sorted_array.extend(array_left[li:])
            break
        if li >= len(array_left):
            sorted_array.extend(array_right[ri:])
            inversion_number += c * len(array_right[ri:])
            break
           
        if array_right[ri] <= array_left[li]:
            sorted_array.append(array_right[ri])
            ri += 1
            inversion_number += li
        else: 
            sorted_array.append(array_left[li])
            li += 1

    return inversion_number, sorted_array
    

n = int(input())
array = [int(num) for num in input().split(' ')]

# array = [3, 2, 5, 9, 4]
# array = [2, 3, 9, 2, 9]
n, sorted_array = find_inversions(array)
print(n)