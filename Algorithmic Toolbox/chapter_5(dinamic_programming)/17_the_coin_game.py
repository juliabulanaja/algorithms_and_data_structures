

def solve_problem(coins: list):
    
    l = 0
    r = len(coins) - 1
    memo = {}

    def inner(l, r):

        if (l, r) in memo:
            return memo[(l, r)]
        if l > r:
            return 0
        if l == r:
            return coins[l]

        left = coins[l] + min(inner(l + 2, r), inner(l + 1, r - 1))
        right = coins[r] + min(inner(l, r - 2), inner(l + 1, r - 1))
        result = max(left, right)
        memo[(l, r)] = result

        return result
    
    return inner(l, r)
        



if __name__ == "__main__":
    coins = [2,	1, 9, 3]
    result = solve_problem(coins)
    print(result)