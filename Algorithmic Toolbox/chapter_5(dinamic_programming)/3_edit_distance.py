

def find_edit_distance(start_string, end_string):

    dp = []
    for i in range(len(end_string) + 1):
        dp.append([i])

    for j in range(1, len(start_string) + 1):
        dp[0].append(j)

    for i in range(1, len(end_string) + 1):
        for j in range(1, len(start_string) + 1):

            if end_string[i - 1] ==  start_string[j - 1]:
                dp[i].append(dp[i - 1][j - 1])
            else:
                insert = dp[i][j - 1] + 1
                delete = dp[i - 1][j] + 1
                replace = dp[i - 1][j - 1] + 1
                dp[i].append(min(insert, delete, replace))
    return dp[-1][-1]


if __name__ == "__main__":

    start_string = 'editing'
    end_string = 'distance'

    # start_string = input()
    # end_string = input()

    result = find_edit_distance(start_string, end_string)
    print(result)