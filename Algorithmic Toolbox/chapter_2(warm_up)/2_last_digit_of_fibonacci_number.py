# Compute the last digit of the n-th Fibonacci number.
# Input. An integer n.
# Output. The last digit of the n-th Fibonacci number.

n = int(input())

def fibonacci_last_digit(n: int) -> int:
    # Handle small cases directly
    if n <= 1:
        return n

    prev, curr = 0, 1

    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 10

    return curr


result = fibonacci_last_digit(n)

print(result)