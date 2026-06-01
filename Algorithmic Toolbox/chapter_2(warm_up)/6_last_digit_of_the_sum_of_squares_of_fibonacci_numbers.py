# Compute the last digit of F0^2 + F1^2 + ··· + Fn^2.
# Input. An integer n.
# Output. The last digit of F0^2 + F1^2 + ··· + Fn^2.

n = int(input())

fibonacci = {}

def fibonacci_last_digit(n: int) -> int:
    # if n <= 1:
    #     return n

    period = 60
    n = n % period

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 10
    return curr


def fibonacci_sum_squares_last_digit(n: int) -> int:
    fn = fibonacci_last_digit(n)
    fn1 = fibonacci_last_digit(n + 1)
    return (fn * fn1) % 10

result = fibonacci_sum_squares_last_digit(n)
print(result)
