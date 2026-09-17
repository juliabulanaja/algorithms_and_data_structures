# python3
# Task. Implement BetterBWMatching algorithm

def get_first_occurrence(first_column: str) -> dict:
    """A dictionary that stores the very first index where each character appears 
    in the sorted first_column. """

    first_occurrence = {}
    for i, char in enumerate(first_column):
        if not char in first_occurrence:
            first_occurrence[char] = i
    return first_occurrence


def get_count_table(last_column: str) -> dict:
    """A precomputed structure that tells you exactly how many times a character 
    has appeared in last_column up to a specific index. """

    unique_chars = sorted(set(last_column))
    n = len(last_column)
    count_table = {char: [0] * (n + 1) for char in unique_chars}

    for i, char in enumerate(last_column):
        for c in count_table:
            count_table[c][i + 1] = count_table[c][i]
        count_table[char][i + 1] += 1
    return count_table


def bw_matching(pattern: str, first_occurrence: dict, count_table: dict) -> int:

    top = 0
    bottom = len(last_column) - 1

    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            if symbol not in first_occurrence:
                return 0

            top = first_occurrence[symbol] + count_table[symbol][top]
            bottom = first_occurrence[symbol] + count_table[symbol][bottom + 1] - 1

        else:
            return bottom - top + 1
    return 0


if __name__ == "__main__":
    last_column = input()
    n = int(input())
    patterns = input().split(" ")

    first_column = "".join(sorted(last_column))

    first_occurrence = get_first_occurrence(first_column)
    count_table = get_count_table(last_column)


    results = []
    for pattern in patterns:
        result = bw_matching(pattern, first_occurrence, count_table)
        results.append(result)

    print(" ".join(map(str, results)))
