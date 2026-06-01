import re

operator_functions = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y

}

def parentheses(numbers, operations):
    M = [[None for _ in range(len(numbers))] for _ in range(len(numbers))]
    m = [[None for _ in range(len(numbers))] for _ in range(len(numbers))]
    n = len(numbers)

    def min_and_max(i, j):

        minimum = float('inf')
        maximum = -float('inf')

        for k in range(i, j):

            a = operator_functions[operations[k]](M[i][k], M[k+1][j])
            b = operator_functions[operations[k]](M[i][k], m[k+1][j])
            c = operator_functions[operations[k]](m[i][k], M[k+1][j])
            d = operator_functions[operations[k]](m[i][k], m[k+1][j])

            minimum = min(minimum, a, b, c, d)
            maximum = max(maximum, a, b, c, d)

        return minimum, maximum


    for i in range(n):
        M[i][i] = numbers[i]
        m[i][i] = numbers[i]
    
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j)

    return M[0][-1]

if __name__ == "__main__":

    expresion = input()
    # expresion = '5-8+7*4-8+9'
    numbers = [int(n) for n in re.findall(r'\d+', expresion)]
    operations = re.findall(r'[-+*/]', expresion)

    result = parentheses(numbers, operations)
    print(result)

