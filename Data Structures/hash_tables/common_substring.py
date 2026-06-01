
import sys


def precompute_hashes(text: str, k: int, x: int, p: int):
    n = len(text)
    
    current_hash = 0
    for i in range(k):
        current_hash = (current_hash * x + ord(text[i])) % p
    hashes = [current_hash % p]

    h = pow(x, k-1, p)

    for i in range(n-k):
        current_hash = (((hashes[i] - ((ord(text[i]) * h)) % p) * x) % p + ord(text[i + k])) % p
        hashes.append(current_hash)

    return hashes


# def precompute_hashes(text: str, prev_hashes: list, k: int, x: int, p: int):

#     if not prev_hashes:
#         return [ord(c) for c in text]

#     hashes = []
#     for i in range(len(prev_hashes)-1):
#         current_hash = ((prev_hashes[i] * x) % p + ord(text[i+k])) % p
#         if current_hash < 0:
#                 current_hash += q
#         hashes.append(current_hash)
#     return hashes


def find_substring(str1, str2):
    x = 256
    p = 10 ** 9 + 7
    p2 = 10 ** 9 + 3

    start1 = 0
    start2 = 0
    length = 0

    l = 1
    r = min(len(str1), len(str2))

    while l <= r:

        k = (l + r) // 2
        # print(l, r, k)

        hash1_v1 = precompute_hashes(str1, k, x, p)
        hash2_v1 = precompute_hashes(str2, k, x, p)

        hash1_v2 = precompute_hashes(str1, k, x, p2)
        hash2_v2 = precompute_hashes(str2, k, x, p2)

        found_match = False


        hash_map = {}
        for i in range(len(hash1_v1)):
            key = (hash1_v1[i], hash1_v2[i])
            if key not in hash_map:
                hash_map[key] = i

        for i in range(len(hash2_v1)):
            key = (hash2_v1[i], hash2_v2[i])
            if key in hash_map:
                found_match = True
                start1 = hash_map[key]
                start2 = i
                length = k
                break

        # for i, h_s in enumerate(hash1_v1):
        #     for j, h_b in enumerate(hash2_v1):
        #         if h_s == h_b and hash1_v2[i] == hash2_v2[j]:
        #             found_match = True
        #             start1 = i
        #             start2 = j
        #             length = k
        #             break
        #     if found_match:
        #         break

        if found_match:
            l = k + 1
        else: 
            r = k - 1

    return ' '.join(map(str, [start1, start2, length]))
        



if __name__ == "__main__":

    # data = []
    # while True:
    #     q = input()
    #     if q == '':
    #         break
    #     data.append(q.split(' '))



    for line in sys.stdin:
        s, t = line.strip().split()
        print(find_substring(s, t))

