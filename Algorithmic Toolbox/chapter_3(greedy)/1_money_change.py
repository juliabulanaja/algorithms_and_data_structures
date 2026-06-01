
money = int(input())

def change(money: int) -> int:
    tens = money // 10
    money %= 10

    fives = money // 5
    money %= 5

    ones = money

    return tens + fives + ones

result = change(money)
print(result)
        