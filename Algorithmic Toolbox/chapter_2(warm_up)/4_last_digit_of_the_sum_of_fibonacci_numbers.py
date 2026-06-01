# Compute the last digit of F0 + F1 + ··· + Fn.
# Input. An integer n.
# Output. The last digit of F0 + F1 + ··· + Fn

n = int(input())

def fibonacci_number(n: int) -> int:

    if n <= 1:
        return n

    # Pisano period for modulo 10
    period = 60

    n = (n + 2) % period

    prev, curr = 0, 1
    for _ in range(n-1):
        prev, curr = curr, (prev + curr) % 10

    return (curr - 1) % 10


print(fibonacci_number(n))