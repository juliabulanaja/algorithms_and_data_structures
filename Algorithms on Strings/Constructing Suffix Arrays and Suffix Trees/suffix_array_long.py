# python3
# Task. Construct the suffix array of a string.


def construct_suffix_array(string: str) -> list:
    order = sort_characters(string)
    classes = compute_char_classes(string, order)
    l = 1
    while l < len(string):
        order = sort_doubled(string, l, order, classes)
        classes = update_classes(order, classes, l)
        l = l * 2
    return order


def sort_characters(string: str) -> list:
    n = len(string)
    alphabet_size = 256
    order = [None] * n
    count = [0] * alphabet_size

    # Count occurrences of each character
    for char in string:
        count[ord(char)] += 1

    # Compute cumulative counts
    for j in range(1, alphabet_size):
        count[j] += count[j - 1]

    # Place characters in order array from right to left
    for i in range(len(string) - 1, -1, -1):
        c = ord(string[i])
        count[c] -= 1
        order[count[c]] = i

    return order


def compute_char_classes(string: str, order: list) -> list:
    n = len(string)
    classes = [None] * n
    classes[order[0]] = 0

    for i in range(1, n):
        if string[order[i]] != string[order[i - 1]]:
            classes[order[i]] = classes[order[i - 1]] + 1
        else:
            classes[order[i]] = classes[order[i - 1]]
    # print(classes)
    return classes


def sort_doubled(string: str, l: int, order: list, classes: list) -> list:
    n = len(string)
    count = [0] * n
    new_order = [None] * n
    for i in range(n):
        count[classes[i]] = count[classes[i]] + 1

    for j in range(1, n):
        count[j] = count[j] + count[j - 1]

    for i in range(n - 1, -1, -1):
        start = (order[i] - l + n) % n
        cl = classes[start]
        count[cl] = count[cl] - 1
        new_order[count[cl]] = start
    
    return new_order


def update_classes(new_order: list, classes: list, l: int) -> list:
    n = len(new_order)
    new_classes = [None] * n
    new_classes[new_order[0]] = 0

    for i in range(1, n):
        cur = new_order[i]
        prev = new_order[i - 1]

        mid = (cur + l) % n
        mid_prev = (prev + l) % n

        if classes[cur] != classes[prev] or classes[mid] != classes[mid_prev]:
            new_classes[cur] = new_classes[prev] + 1
        else:
            new_classes[cur] = new_classes[prev]
    
    return new_classes
 


if __name__ == "__main__":
    text = input()

    result = construct_suffix_array(text)
    print(' '.join(map(str, result)))


