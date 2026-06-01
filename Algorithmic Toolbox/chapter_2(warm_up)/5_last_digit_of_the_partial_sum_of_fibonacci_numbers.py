# Compute the last digit of Fm + Fm+1 + ··· + Fn.
# Input. Integers m ≤ n.
# Output. The last digit of Fm + Fm+1 + ··· + F

m, n = [int(num) for num in input().split(' ')]


def fibonacci_last_digit(n) -> int:

    if n <= 1:
        return n

    period = 60
    n =  n % period

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 10
    return curr


def fibonacci_partial_sum_last_digit(m: int, n: int) -> int:

    last_n = fibonacci_last_digit(n + 2)
    last_m = fibonacci_last_digit(m + 1)

    return (last_n - last_m) % 10

result = fibonacci_partial_sum_last_digit(m, n)
print(result)