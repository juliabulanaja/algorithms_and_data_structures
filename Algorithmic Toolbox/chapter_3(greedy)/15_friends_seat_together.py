import statistics 
       

positions = [1, 3, 7]
# positions = [2, 4, 6, 8] 
# positions = [10, 1, 7, 4] # -> [4, 5, 6, 7]. Minimum moves: 8
# positions = [1, 10]
# positions = [1, 3, 6]
# positions = [3, 8, 9]
# positions = [5, 6, 7, 20] 


def change_seats2(positions):
    positions.sort()
    median = int(statistics.median(positions))
    n = len(positions)
    k = n // 2

    # print(median, n, k)

    new_positions = list(range(median - k, median + k + 1))
    if n % 2 == 0:
        new_positions_1 = new_positions[1:]
        new_positions_2 = new_positions[:-1]

        steps_1 = sum(abs(x - y) for x, y in zip(new_positions_1, positions))
        steps_2 = sum(abs(x - y) for x, y in zip(new_positions_2, positions))

        if steps_1 < steps_2:
            print('with first')
            return steps_1, new_positions_1
        else:
            print('with last')
            return steps_2, new_positions_2


    steps = sum(abs(x - y) for x, y in zip(new_positions, positions))
    return steps, new_positions


# steps, new_positions = change_seats2(positions)
# print(steps, new_positions)


def change_seats3(positions):
    positions.sort()
    n = len(positions)
    
    adjusted = [p - i for i, p in enumerate(positions)]
    start = int(statistics.median(adjusted))

    new_positions = [start + i for i in range(n)]
    # new_positions = [abs(x - median) for x in adjusted]

    print(f"positions: {positions}")
    print(f"adjusted: {adjusted}")
    print(f"median: {start}")
    print(f"new_positions: {new_positions}")

    return sum(abs(x - y) for x, y in zip(new_positions, positions))


result = change_seats3(positions)
print(result)

# x, x+1, x+2 ...
# p[i] - (x + i)
# p[i] - i
