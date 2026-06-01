bulbs = [0, 1, 0, 1]
bulbs = [1, 1, 1, 1]
bulbs = [1, 0, 0, 1, 0]
bulbs = [1, 0, 0, 0, 0]

def turn_on_bulbs(bulbs: list) -> int:
    switched = False
    switch_count = 0

    for i in range(len(bulbs)):

        if (bulbs[i] == 0 and not switched) or (bulbs[i] == 1 and switched):
            # bulbs[i] = 1
            switched = not switched
            switch_count += 1
    
    return switch_count


result = turn_on_bulbs(bulbs)
print(result)