compounds, W = [int(num) for num in input().split(' ')]

costs = []

for _ in range(compounds):
    cost, weight = [int(num) for num in input().split(' ')]
    costs.append((cost, weight))

costs = sorted(costs, key=lambda item: item[0] / item[1], reverse=True) 

def fractional_knapsack(costs: list, W: int) -> float:

    result = 0.0
    for cost, weight in costs:   
        if W == 0:
            break    

        take = min(W, weight)
        result += take * (cost / weight)
        W -= take

    return result

result = fractional_knapsack(costs, W)
print(result)
