# There are N people standing in a circle waiting to be executed. The counting out begins at some point in the circle and proceeds around the circle in a fixed direction. In each step, a certain number of people are skipped and the next person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom. 

# Given the total number of persons N and a number k which indicates that k-1 persons are skipped and the kth person is killed in a circle. The task is to choose the person in the initial circle that survives.

# The rule is: If the number of people n is a perfect power of 2 (like 2, 4, 8, 16...), the person at position 1 always wins.If n is not a power of 2, we write n as 2^m + l (where 2^m is the largest power of 2 less than n). The winning position W(n) is"

# W(n) = 2l + 1
import math
import time

k = 3
n = 7

people = [i for i in range(1, n+1)]

def josephus_recursive(people: list, k: int, index = 0):

    if len(people) == 1:
        return people[0]
        
    index = (index + k - 1) % len(people) 
    people.pop(index)

    return josephus_recursive(people=people, k=k, index=index)


winner = josephus_recursive(people, k)
# print(winner)

def Josephus(n, k):

    # initialize two variables i and answer
    i = 1
    answer = 0
    while(i <= n):
        
        print("_______________________")
        print("i: ", i)
        print("answer: ", answer, end="\n\n")

        # update the value of answer
        print(f"(answer + k) % i ")
        print(f"({answer} + {k}) % {i} == {(answer + k) % i}")

        answer = (answer + k) % i
        
        i += 1
        print("answer: ", answer)
    
    # returning the required answerwer
    return answer + 1


n = 14
k = 2

result = Josephus(n, k)

print("_______________________")
print(result)


