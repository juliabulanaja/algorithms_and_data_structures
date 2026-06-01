from time import perf_counter


def solve_problem(n):

    n = n * 2
    dp = {0: 1, 1: 1, 2: 1}

    def inner(n):
        if n in dp:
            return dp[n]
        
        ways = 0

        for i in range(2, n+1, 2):
            left_n = n - i
            right_n = i - 2

            left = inner(left_n)
            right = inner(right_n)

            ways += left * right
        
        return ways
    return inner(n)

def solve_problem_tabular(n):
    dp = [[] for i in range(n)]

    for i in dp:
        i.append(1)
    dp[0].append(1)

    for j in range(1, n+1):

        if j <= 2: 
            i = 1 
        else:
            i = j - 1

        while i < len(dp):
            value = sum(dp[i-1])
            dp[i].append(value)
            i += 1
            
    return dp[-1][-1]





if __name__ == "__main__":
    n = 20

    start = perf_counter()
    result = solve_problem(n)
    print(f"Execution time: {perf_counter() - start}. Result: {result}")


    start = perf_counter()
    result2 = solve_problem_tabular(n)
    print(f"Execution time: {perf_counter() - start}. Result: {result2}")