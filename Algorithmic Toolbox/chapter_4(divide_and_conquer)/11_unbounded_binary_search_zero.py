def function(x: int) -> int:
    return 2 * x - 20

def function2(x: int) -> int:
    return 2 * x + 20


def unbounded_binary_search(function: callable) -> int:
    low = 1 
    high = low * 2

    func_value = function(high)

    if func_value > 0:
        return -1

    while func_value <= 0:

        if func_value == 0:
            return high

        low = high + 1
        high = low * 2
        func_value = function(high)

    while low <= high:

        middle = (high - low) // 2 + low
        func_value = function(middle)
        if func_value == 0:
            return middle
        elif func_value > 0:
            high = middle - 1
        else:
            low = middle + 1
    




if __name__ == "__main__":
    # result = unbounded_binary_search(function)
    # print(result)

    result2 = unbounded_binary_search(function2)
    print(result2)