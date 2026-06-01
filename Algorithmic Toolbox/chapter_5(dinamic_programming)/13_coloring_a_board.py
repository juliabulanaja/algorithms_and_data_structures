def solve_problem(n: int):

    aba = 12
    abc = 24
    
    for _ in range(n-1):
        next_aba = 7 * aba + 5 * abc
        next_abc = 10 * aba + 11 * abc
        abc, aba = next_abc, next_aba
        print(abc + aba)


if __name__ == "__main__":
    result = solve_problem(4)
    print(result)