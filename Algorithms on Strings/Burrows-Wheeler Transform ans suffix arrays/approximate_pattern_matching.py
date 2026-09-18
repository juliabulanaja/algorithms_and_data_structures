def bwt(string: str) -> str:
    """ Finds a last_column. """
    
    result = [string]
    n = len(string)
    for i in range(1, n):
        new_string = string[i:] + string[:i]
        result.append(new_string)

    result.sort()
    return "".join([s[-1] for s in result])


def construct_suffix_array(text: str) -> None:
    suffixes = []
    for i in range(len(text)):
        suffixes.append((i, text[i:]))

    sorted_pairs = sorted(suffixes, key=lambda item: item[1])
    sorted_pairs = {i: el[0] for i, el in enumerate(sorted_pairs) if el[0] % 5 == 0}

    return sorted_pairs


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


def bw_matching(pattern: str, d: int, first_occurrence: dict, count_table: dict, last_column: str, first_column: str) -> list:

    n = len(last_column)
    current_symbol = pattern[-1]
    pattern = pattern[:-1]
    mismatches = {i: int(char != current_symbol) for i, char in enumerate(first_column)}

    while pattern:
        new_mismatches = {}
        current_symbol = pattern[-1]
        pattern = pattern[:-1]

        for i, m in mismatches.items():
            new_char = last_column[i]
            current_mismatch = m + (1 if new_char != current_symbol else 0)

            if current_mismatch <= d:
                new_index = first_occurrence[new_char] + count_table[new_char][i] 
                new_mismatches[new_index] = current_mismatch

        mismatches = new_mismatches
    return mismatches



def find_position(first_column_index: int, suffix_array: dict, first_occurrence: dict, count_table: dict, last_column: str) -> int:

    next_index = first_column_index
    steps = 0
    while next_index is not None:
        if next_index in suffix_array:
            return suffix_array[next_index] + steps

        next_char = last_column[next_index]
        next_index = first_occurrence[next_char] + count_table[next_char][next_index] 
        steps += 1
    
    return -1
 

if __name__ == "__main__":
    # text = input()
    # pattern = input()
    # d = int(input())

    text = "$AACACG"
    pattern = "ACA"
    d = 1

    last_column = bwt(text)
    first_column = "".join(sorted(last_column))

    first_occurrence = get_first_occurrence(first_column)
    count_table = get_count_table(last_column)
    suffix_array = construct_suffix_array(text)

    indexes = bw_matching(pattern, d, first_occurrence, count_table, last_column, first_column)

    for index in indexes:
        result = find_position(index, suffix_array, first_occurrence, count_table, last_column)
        print(result)