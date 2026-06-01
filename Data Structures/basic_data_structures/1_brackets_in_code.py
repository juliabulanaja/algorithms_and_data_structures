
def solve_problem(data: str):
    pattern = {'}': '{', ']': '[', ')': '('}

    stack = []
    for i in range(len(data)):
        symbol = data[i]

        if symbol in pattern.values():
            stack.append((symbol, i))

        elif symbol in pattern.keys():
            if not stack or stack[-1][0] != pattern[symbol]:
                return i + 1

            stack.pop()

    if len(stack) == 0:
        return "Success"
    return stack[-1][1] + 1


if __name__ == "__main__":

    data = input()
    # data = '{}[]'
    # data = '[()]'
    # data = '(())'
    # data = '{[]}()'
    # data = '{'
    # data = '{[}'
    # data = 'foo(bar);'
    # data = 'foo(bar[i);'
    # data = '[](()'
    result = solve_problem(data)
    print(result)