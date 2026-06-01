# Compute the n-th Fibonacci number modulo m.
# Input. Integers n and m.
# Output. n-th Fibonacci number modulo m
# import math 


n, m = [int(num) for num in input().split(' ')]


# def pow(x, n):
#     if n == 0:
#         return 1

#     #  // Handle negative exponents: x^-n = 1 / x^n

    # if n < 0:
    #     x = 1 / x
    #     n = -1 * n 

    # answer = 1
    # while n > 0:
    #     if n % 2 != 0:
    #         answer *= x

    #     x = x ** 2
    #     n = n / 2

    # return answer


# def fibonacci_binet(n, m):
#     if n < 0:
#         return 0
#     phi = (1 + math.sqrt(5)) / 2
#     psi = (1 - math.sqrt(5)) / 2
#     # The result is rounded to the nearest integer as F(n) is always an integer
#     return round((pow(phi, n) - pow(psi, n)) / math.sqrt(5)) % m
 
def pisano_period(m: int) -> int:
    prev, curr = 0, 1
    for i in range(m * m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1


def fibonacci_mod(n: int, m: int) -> int:
    if n <= 1:
        return n % m

    period = pisano_period(m)
    n %= period

    # VERY IMPORTANT EDGE CASE
    if n == 0:
        return 0

    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % m

    return curr


result = fibonacci_mod(n, m)
print(result)