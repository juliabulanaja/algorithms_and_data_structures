# Compute the n-th Fibonacci number.
# Input. An integer n.
# Output. n-th Fibonacci number.

n = int(input())
fibonacci = {}

def find_fibonacci_number(n: int) -> int:
    
    global fibonacci

    if n in fibonacci.keys():
        return fibonacci[n]

    if n <= 1:
        fibonacci[n] = n
        return n

    result = find_fibonacci_number(n-2) + find_fibonacci_number(n-1)
    fibonacci[n] = result
    return result

result = find_fibonacci_number(n)
print(result)