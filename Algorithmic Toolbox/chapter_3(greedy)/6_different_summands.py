n = int(input())

# n = 2
def different_summands(n: int) -> list[int]:
    
    result = []

    for i in range(1, n+1):

        if  n - i <= i:
            result.append(n)
            break
        
        n -= i
        result.append(i) 


    return result


result = different_summands(n)
print(len(result))
print(*result)

# 2 -> [2]
# 4 -> [1, 3]
# 6 -> [1, 2, 3]

