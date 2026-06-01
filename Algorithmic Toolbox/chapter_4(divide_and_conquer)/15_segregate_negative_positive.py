
def segregate_numbers(array: list) -> list:

    start = 0
    end = len(array) - 1

    if len(array) <= 1:
        return array

    middle = (start + end) // 2
    left = segregate_numbers(array[:middle+1])
    right = segregate_numbers(array[middle+1:])

    l = 0
    r = 0
    result = []

    for _ in range(len(left) + len(right)):
        if l < len(left) and left[l] < 0:
            result.append(left[l])
            l += 1
        elif r < len(right) and right[r] < 0:
            result.append(right[r])
            r += 1
        else:
            result.extend(left[l:])
            result.extend(right[r:])
            break

    return result


if __name__ == "__main__":
    array = [17, 11, -3, -16, 17, 15, 17, -5, -18, 6]

    result = segregate_numbers(array)
    print(result)