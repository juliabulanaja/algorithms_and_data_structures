def solve_problem(W: int, weights: list[int]):

    dp = [[0] * (W + 1) 
        for _ in range(len(weights) + 1)] 
        
    for i in range(1, len(dp)):
        current_weight = weights[i-1]

        for j in range(1, W + 1):
            current_capacity = j
                    
            if current_weight > current_capacity:
                dp[i][j] = dp[i-1][j]
            else: 
                prev_value = dp[i-1][j]
                new_value = current_weight + dp[i-1][current_capacity-current_weight]
                
                dp[i][j] = max(new_value, prev_value)

    return dp[-1][-1]


if __name__ == "__main__":
    # W = 10
    # weights = [1, 4, 8]

    W, n = [int(i) for i in input().split(" ")]
    weights = [int(i) for i in input().split(" ")]

    result = solve_problem(W, weights)
    print(result)