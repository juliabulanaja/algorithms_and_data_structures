coins = [1, 2, 4, 10]
coins = [1, 2, 2, 5]
coins = [1]
coins = [1, 2, 3]
coins = [1, 1, 1, 1]
coins = [2, 3, 4]
coins = [5, 7, 8]
coins = [1, 2, 5]
coins = [1, 3, 4]
coins = [1, 1, 3, 4]
coins = [1, 2, 4, 8]
coins = [1, 2, 4, 9]
coins = [1, 1, 2, 6]
coins = [1, 1, 3, 5, 7, 22]

def solve_problem(coins: list) -> int:
    coins.sort()
    minimum = 0

    for coin in coins:
        if coin > minimum + 1:
            return minimum + 1
        
        minimum += coin
    return minimum + 1

result = solve_problem(coins)
print(result)