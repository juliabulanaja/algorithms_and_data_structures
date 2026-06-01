def plus_one(x):
    return x - 1

def mul_2(x): 
    return x / 2

def mul_3(x):
    return x / 3

operations = [
    plus_one, mul_2, mul_3
]

def find_min_operations(number):
    dp = {key: float('inf') for key in range(1, number + 1)}
    dp[1] = 0

    for i in range(2, number + 1):
        for operation in operations:
            value = operation(i)

            if value % 1 == 0 and dp[value] + 1 < dp[i]:
                dp[i] = dp[value] + 1

    
    return dp[number]

if __name__ == "__main__":
    number = int(input())
    # number = 96234

    result = find_min_operations(number)
    print(result)
