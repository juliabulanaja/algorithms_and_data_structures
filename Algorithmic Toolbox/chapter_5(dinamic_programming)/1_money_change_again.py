
def count_coins_memo(amount, memo={0: 0}):
    if amount in memo:
        return memo[amount]
    if amount < 1:
        return 0

    value = min([count_coins_memo(amount - coin, memo) + 1 for coin in coins])
    memo[amount] = value
    return value


def count_coins(amount):

    if amount < 1:
        return 0

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[amount] == float('inf'): 
        return -1
    return dp[amount] 




if __name__ == "__main__":
    coins = [1, 3, 4]
    # amount = 34
    amount = int(input())
    # result = count_coins_memo(amount)
    # print(result)

    result2 = count_coins(amount)
    print(result2)
