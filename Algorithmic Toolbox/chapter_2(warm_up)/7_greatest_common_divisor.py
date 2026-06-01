# Compute the greatest common divisor of two positive integers.
# Input. Two positive integers a and b.
# Output. The greatest common divisor of a and b.

a, b = [int(num) for num in input().split(" ")]

def gcd(a: int, b: int):
    if b == 0:  
        return a
    a, b = b, a - b* (a // b)
    return gcd(a, b)

print(gcd(a, b))