def solve_problem(array1, array2):

    dp = []
    for i in range(len(array1) + 1):
        dp.append([0])
    for j in range(1, len(array2) + 1):
        dp[0].append(0)

    for i in range(1, len(array1) + 1):
        for j in range(1, len(array2) + 1):

            if array1[i - 1] == array2[j - 1]:
                dp[i].append(dp[i - 1][j - 1] + 1)
            else:
                max_value = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                dp[i].append(max_value)
    return dp[-1][-1]


if __name__ == "__main__":

    n = int(input())
    array1 = [int(i) for i in input().split(' ')]
    m = int(input())
    array2 = [int(i) for i in input().split(' ')]

    result = solve_problem(array1, array2)
    print(result)