n = int(input())

sequence_1 = [int(num) for num in input().split(' ')]
sequence_2 = [int(num) for num in input().split(' ')]

def dot_product(sequence_1: list, sequence_2: list) -> int:
    sequence_1 = sorted(sequence_1, reverse=True)
    sequence_2 = sorted(sequence_2, reverse=True)

    return sum([a * b for a, b in zip(sequence_1, sequence_2)]) 

result = dot_product(sequence_1, sequence_2)
print(result)