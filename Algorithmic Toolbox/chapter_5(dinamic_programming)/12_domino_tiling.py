def solve_problem(n: int):
    if n % 2 != 0:
        return 0

    A = [1, 0]
    B = [0, 3]

    for i in range(2, n):
        a = A[i-2] + B[i-1]
        b = B[i-2] + 2 * A[i-1]
        A.append(a)
        B.append(b)

    return B[-1]


if __name__ == "__main__":
    result = solve_problem(10)
    print(result)