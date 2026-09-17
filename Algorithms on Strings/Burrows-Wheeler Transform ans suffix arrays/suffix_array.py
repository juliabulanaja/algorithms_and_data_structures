# python3
# Task. Construct the suffix array of a string.


def construct_suffix_array(text: str) -> None:
    suffixes = []
    for i in range(len(text)):
        suffixes.append((i, text[i:]))

    sorted_pairs = sorted(suffixes, key=lambda item: item[1])
    sorted_indexes = [pair[0] for pair in sorted_pairs]
    print(' '.join(map(str, sorted_indexes)))


if __name__ == "__main__":
    text = input()
    construct_suffix_array(text)
