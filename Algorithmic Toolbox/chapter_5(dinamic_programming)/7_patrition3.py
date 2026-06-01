
def brute_force_solution(sequence: list[int]):

    total = sum(sequence)
    if total % 3 != 0:
        return 0

    target = total / 3
    subsets = [0, 0, 0]

    def inner(index: int):
        if index == len(sequence):
            return int(subsets[0] == subsets[1] == subsets[2] == target)

        for i in range(3):

            if subsets[i] + sequence[index] <= target:
                subsets[i] += sequence[index]
                if inner(index + 1):
                    return 1
                subsets[i] -= sequence[index]  
            if subsets[i] == 0:
                break

        return 0 

    return inner(0)
    

if __name__ == "__main__":
    n = int(input())
    sequence = [int(i) for i in input().split()]

    # sequence = [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]
    # sequence = [3, 3, 4, 1, 1]
    result = brute_force_solution(sequence)
    print(result)