def solve_problem_recursively(costs):

    n = len(costs)
    m = len(costs[0])

    if n == 0:
        return 0
    if n == 1:
        return min(costs)

    memo = {}

    def inner(house_idx=0, prev_color_idx=None, first_color_idx=None):

        state = (house_idx, prev_color_idx, first_color_idx)
        if state in memo:
            return memo[state]

        minimum_cost = float('inf')

        if house_idx == n - 1:          # base case
            for color_idx in range(m):
                if color_idx not in [prev_color_idx, first_color_idx]:
                    minimum_cost = min(minimum_cost, costs[house_idx][color_idx])
                    memo[state] = minimum_cost
        elif house_idx == 0:            #start
            for color_idx in range(m):
                color_price = costs[0][color_idx] + inner(1, color_idx, color_idx)
                minimum_cost = min(minimum_cost, color_price)
                memo[state] = minimum_cost
        else:
            for color_idx in range(m):
                if color_idx != prev_color_idx:
                    color_price = costs[house_idx][color_idx] 
                    price = color_price + inner(house_idx + 1, color_idx, first_color_idx)
                    minimum_cost = min(minimum_cost, price)
                    memo[state] = minimum_cost

        return minimum_cost
    return inner()


if __name__ == "__main__":

    costs = [
        [7, 3, 8],   # house 0
        [5, 6, 7],   # house 1
        [2, 4, 3],   # house 2
        [10, 1, 5]   # house 3
    ]

#     costs = [
#     [1, 9, 9, 9], # House 0
#     [9, 1, 9, 9], # House 1
#     [9, 9, 1, 9], # House 2
#     [9, 9, 9, 1], # House 3
#     [1, 9, 9, 9]  # House 4 (Conflicts with House 0)
# ]
    result = solve_problem_recursively(costs)
    print(result)

