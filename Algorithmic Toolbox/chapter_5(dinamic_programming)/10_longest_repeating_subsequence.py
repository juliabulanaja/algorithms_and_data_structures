def solve_prodlem(string: str):

    n = len(string)
    dp = [[0]*(n+1) for _ in range(n)]
    left = 1
    i = 1

    while i <= n:
        j = i + 1

        while j <= n:
            if string[i-1] == string[j-1]:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            j += 1
        i += 1


    i = n - 1
    right = i + 1

    sequence = []
    while i > 0:  
        j = right
        while j > i:
            # print(dp[i-1][j-1], dp[i-1][j], dp[i][j],  dp[i][j-1])
            if dp[i-1][j-1] == dp[i-1][j] == (dp[i][j] - 1) and dp[i][j] != dp[i][j-1]:
                sequence.insert(0, string[j-1])
                right = j - 1
                break
            else:
                j -= 1
        i -= 1
    
    return sequence


if __name__ == "__main__":
    string = 'acacbbeb'
    result = solve_prodlem(string)
    print(result)