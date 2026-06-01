

def solve_problem_greedy(first: str, second: str, target: str) -> str | int:
    
    i = 0
    j = 0

    for letter in target:
        if i < len(first) and letter == first[i]:
            i += 1
        elif j < len(second) and letter == second[j]:
            j += 1
        else:
            return -1

    return target


def solve_problem_dp(first: str, second: str, target: str) -> str | int:
    
    if len(first) + len(second) != len(target):
        return -1

    first = ' ' + first
    second = ' ' + second
    target = ' ' + target

    dp = [[False] * (len(second)) for _ in range(len(first))]

    for i in range(len(second)):
        if target[i] == second[i]:
            dp[0][i] = True
        else:
            break

    for i in range(len(first)):
        if target[i] == first[i]:
            dp[i][0] = True
        else:
            break


    for i in range(1, len(first)):
        for j in range(1, len(second)):
            index = i + j

            if dp[i][j-1]:
                dp[i][j] = second[j] == target[index]

            elif dp[i-1][j]:
                dp[i][j] = first[i] == target[index]

    return target.strip() if dp[-1][-1] else -1       




if __name__ == "__main__":
    # a = "tree"
    # b = "sort"
    # c = "tsroerte"

    a = "aab"
    b = "ac"
    c = "aacab"

    # result = solve_problem_greedy(a, b, c)
    # print(result)

    result = solve_problem_dp(a, b, c)
    print(result)