import sys


def precompute_hashes(text, x, p):
   
    hashes = [0]
    for i in range(len(text)):
        h = (hashes[i] * x) % p + ord(text[i]) % p
        hashes.append(h)
    return hashes

def find_hash_to_compare(h_s, index, pattern_size, x, p, powers):
    # return (h_s[index] - h_s[index-pattern_size] * pow(x, pattern_size, p) + p) % p
    return (h_s[index] - h_s[index-pattern_size] * powers[pattern_size] + p) % p


def find_error_index(left, right, h_s, h_p, x, p, index, powers):

    while left <= right:
        middle = (right - left) // 2 + left
        pattern_size = middle - left + 1

        hash_to_compare = find_hash_to_compare(h_s, middle, pattern_size, x, p, powers)
        hash_pattern = find_hash_to_compare(h_p, middle-index+1, pattern_size, x, p, powers) 

        if hash_to_compare == hash_pattern and left == right:
            return left, False

        if hash_to_compare == hash_pattern:
            left = middle + 1
        else:
            right = middle - 1

    return left, True


def match_find_substring(k, string, pattern):
    k = int(k)
    x = 31 # 256
    p = 1_000_000_007 # 10 * 9 + 7
    
    h_s = precompute_hashes(string, x, p)
    h_p = precompute_hashes(pattern, x, p)
    pattern_size = len(pattern)
    powers = [pow(x, i, p) for i in range(pattern_size+1)]
    pattern_full_hash = h_p[-1]
    result = []

    for i in range(1, len(h_s)-pattern_size+1):
        hash_to_compare = find_hash_to_compare(h_s, i+pattern_size-1, pattern_size, x, p, powers)
        errors = 0  

        if hash_to_compare == pattern_full_hash:
            result.append(i-1)
            continue
    
        left = i
        right = i + pattern_size - 1
        
        # print(i, string[i-1: right], pattern)
        
        while left <= right:
            current_index, is_mismatch = find_error_index(left, right, h_s, h_p, x, p, i, powers)
            if is_mismatch:
                errors += 1

            left = current_index + 1
            if errors > k:
                break

        if errors <= k:
            result.append(i-1)

    print(f"{len(result)} {' '.join(map(str, result))}")


if __name__ == "__main__":
    for line in sys.stdin:
        k, s, p = line.strip().split()
        match_find_substring(k, s, p)

 

    
