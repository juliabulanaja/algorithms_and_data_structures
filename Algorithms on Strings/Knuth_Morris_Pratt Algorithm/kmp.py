# python3
# Task. Find all occurrences of a pattern in a string

def kmp(pattern: str, genome: str) -> list:
    n = len(genome)
    m = len(pattern)

    if m > n:
        return []
    if m == n:
        return [0] if pattern == genome else []
    if pattern == '':
        return []

    lps = get_lps(pattern)

    i = 0
    j = 0
    results = []
    current_j = 0

    while i < n:
        if genome[i] == pattern[j]:
            j += 1
            i += 1  

        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == m:
            results.append(i - m)
            j = lps[j - 1]
            
    return results


def compute_prefixes(p: str) -> list:
    n = len(pattern)
    s = [0] * n
    border = 0

    for i in range(1, n):
        while (border > 0) and (p[i] != p[border]):
            border = s[border - 1]
        if p[i] == p[border]:
            border = border + 1
        else:
            border = 0
        s[i] = border

    return s


def get_lps(pattern: str) -> list:
    n = len(pattern)
    lps = [0] * n
    i = 1
    j = 0

    while i < n:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j > 0:
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1

    return lps
        

if __name__ == "__main__":
    pattern = input()
    genome = input()

    results = kmp(pattern, genome)
    print(" ".join(map(str, results)))
