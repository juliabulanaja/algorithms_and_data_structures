
def solve_problem(parents): # too many resursion
    n = len(parents)
    depth = [0] * n

    def inner(index):

        if depth[index] > 0:
            return depth[index]

        if parents[index] == -1:
            depth[index] = 1
            return 1

        else:
            value = 1 + inner(parents[index])
            depth[index] = value
            return value

    
    max_depth = 0
    for i in range(n):
        value = inner(i)
        max_depth = max(max_depth, value)
    return max_depth


def solve_problem_depth(nodes): # Time used: 5.22/3.00

    root = -1
    root_index = None

    for i in range(len(nodes)):
        if nodes[i] == root:
            root_index = i
            break
    if root_index == None:
        return 'No root index'

    parents = [root_index]
    depth = 1

    while parents:
        new_level = []
        for i, node in enumerate(nodes):
            if node in parents:
                new_level.append(i)

        if new_level:
            depth += 1
        parents = new_level

    return depth


def solve_problem_dp(nodes): # correct
    root = -1
    dp = [0] * len(nodes)

    max_deph = 0

    for i in range(len(nodes)):
        current_node = nodes[i]
        current_depth = 1
        while current_node != root:

            if dp[current_node]:
                current_depth += dp[current_node]
                break

            current_node = nodes[current_node]
            current_depth += 1
        max_deph = max(max_deph, current_depth)
        dp[i] = current_depth
    return max_deph


if __name__ == "__main__":
    n = int(input())
    parents = [int(i) for i in input().split()]
    # parents = [4, -1, 4, 1, 1]
    # parents = [-1, 0, 4, 0, 3]


    # result = solve_problem(parents)
    # print(result)

    # result2 = solve_problem_depth(parents)
    # print(result2)

    result3 = solve_problem_dp(parents)
    print(result3)
