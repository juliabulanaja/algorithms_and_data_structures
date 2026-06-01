import random 


def find_pattern(pattern, text):
    l = len(pattern)
    n = len(text)

    if l > n: 
        return []
    if l == 0: 
        return []

    x = 256
    p = 10**9 + 7
    h = pow(x, l-1, p)

    pattern_hash = 0
    current_hash = 0
    for i in range(l):
        pattern_hash += ord(pattern[i]) * pow(x, l-i-1, p)
        current_hash += ord(text[i]) * pow(x, l-i-1, p)

    pattern_hash = pattern_hash % p
    current_hash = current_hash % p
    

    positions = []
    for i in range(n-l+1):
        if pattern_hash == current_hash:
            if pattern == text[i: i+l]:
                positions.append(i)
        
        if i < n - l:
            current_hash = (((current_hash - ((ord(text[i]) * h)) % p) * x) % p + ord(text[i + l])) % p

    return ' '.join(map(str, positions))

        

if __name__ == "__main__":
    pattern = input()
    text = input()

    # pattern = 'aba'
    # text = 'abacaba'
    result = find_pattern(pattern, text)
    print(result)

