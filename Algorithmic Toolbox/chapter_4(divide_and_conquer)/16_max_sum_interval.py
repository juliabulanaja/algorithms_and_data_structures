

def find_max_sum(array: list) -> int:

    max_sum = 0
    current_sum = 0
    
    for num in array:
        if num > current_sum + num:
            current_sum = num
        else: 
            current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum



if __name__ == "__main__":
    array = [7, 3, 2, 0, 5, 4, -10]
    #array = [-7, 3, -2, 0, 7, -5, 4]
    #array = [-7, -3, -2, -10, -7, -5, -4]
    result = find_max_sum(array)
    print(result)