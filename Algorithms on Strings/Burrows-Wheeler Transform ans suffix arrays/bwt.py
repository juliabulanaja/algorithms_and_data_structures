# python3
# Task. Construct the Burrows–Wheeler transform of a string.

def bwt(string: str) -> str:
    result = [string]
    n = len(string)
    for i in range(1, n):
        new_string = string[i:] + string[:i]
        result.append(new_string)

    result.sort()
    return "".join([s[-1] for s in result])



if __name__ == "__main__":
    string = input()
    result = bwt(string)
    print(result)
