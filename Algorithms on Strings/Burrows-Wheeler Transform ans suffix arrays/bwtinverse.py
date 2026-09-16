# python3
# Task. Reconstruct a string from its Burrows–Wheeler transform.

def reconstruct(last_string: str) -> str:
    n = len(last_string)
    first_string = sorted(last_string)

    first_counts = {}
    last_counts = {}

    first_positions = {}
    for i, char in enumerate(first_string):
        count = first_counts.get(char, 0)
        first_counts[char] = count + 1
        first_positions[(char, count)] = i
        
    shortcuts = [0] * n
    for i, char in enumerate(last_string):
        count = last_counts.get(char, 0)
        last_counts[char] = count + 1
        shortcuts[i] = first_positions[(char, count)]

    reconstructed = [first_string[0]]
    next_index = 0

    while len(reconstructed) < n:
        reconstructed.append(last_string[next_index])
        next_index = shortcuts[next_index]

    return "".join(reversed(reconstructed)) 


if __name__ == "__main__":
    string = input()
    result = reconstruct(string)
    print(result)
