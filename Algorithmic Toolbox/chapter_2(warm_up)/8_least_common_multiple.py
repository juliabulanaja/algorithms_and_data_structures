# Compute the least common multiple of two positive integers.
# Input. Two positive integers a and b.
# Output. The least common multiple of a and b.

a, b = [int(num) for num in input().split(" ")]


def gcd(a: int, b: int) -> int:
    if b == 0:  
        return a
    a, b = b, a - b * (a // b)
    return gcd(a, b)

def lcm(a: int, b: int) -> int:
    return int(a * b / gcd(a, b))

print(lcm(a, b))
