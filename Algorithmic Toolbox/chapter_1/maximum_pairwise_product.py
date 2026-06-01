import random 
from time import perf_counter


def find_max_with_sorting(numbers: list):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]


def find_max_with_one_loop(numbers):
    max_1 = max(numbers[0], numbers[1])
    max_2 = min(numbers[0], numbers[1])

    for number in numbers:
        if number > max_1 or number > max_2:
            if max_1 > max_2:
                max_2 = number
            else:
                max_1 = number
    
    return max_1 * max_2

def find_max_with_two_loops(numbers):
    index = 0
    n = len(numbers)

    for i in range(1, n):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[n-1] = numbers[n-1], numbers[index]
    
    index = 0
    for i in range(1, n-1):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[n-2] = numbers[n-2], numbers[index]
    return numbers[n-2] * numbers[n-1]

def find_max_with_two_loops_2(numbers):
    index = 0
    max1 = numbers[0]

    for i, number in enumerate(numbers):
        if number > max1:
            index = i
            max1 = number
    numbers[index] = numbers[-1]
    
    index = 0
    max2 = max(numbers[:-1])
    return max1 * max2

if __name__ == '__main__':

    l = [random.randint(1, 1000) for _ in range(10 ** 7)]
    
    start = perf_counter()
    maximum_1 = find_max_with_sorting(l)
    print(f"Function with sorting finished in {perf_counter() - start} s.")

    start = perf_counter()
    maximum_2 = find_max_with_one_loop(l)
    print(f"Function with one loop finished in {perf_counter() - start} s.")

    start = perf_counter()
    maximum_3 = find_max_with_two_loops(l)
    print(f"Function with two loops finished in {perf_counter() - start} s.")

    start = perf_counter()
    maximum_4 = find_max_with_two_loops_2(l)
    print(f"Function with two loops2 finished in {perf_counter() - start} s.")

    print(maximum_1, maximum_2, maximum_3, maximum_4)