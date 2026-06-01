

def solve_problem(string: str):
    n = len(string)
    dp = [[0]*(n+1) for _ in range(n+1)]

    reversed_str = string[::-1]
    polyndrom = []
    

    for i in range(1, n+1):
        for j in range(1, n+1):

            if string[i-1] == reversed_str[j-1]:
                dp[i][j] = min(dp[i-1][j] + 1, i, j)
            else: 
                dp[i][j] =  max(dp[i-1][j], dp[i][j-1])

    i = n
    j = n
    right = n
    while i > 0:
        while j > 0:
            if dp[i][j-1] == dp[i-1][j] == dp[i-1][j-1] == dp[i][j] - 1:
                polyndrom.append(string[i-1])
                i -= 1
                j -= 1
                right = j
                break

            j -= 1

        if j == 0:
            i -= 1
            j = right

    return polyndrom


if __name__ == "__main__":
    string = 'cmabdama'
    string = 'bbabcbcab'
    result = solve_problem(string)
    print(result)
    