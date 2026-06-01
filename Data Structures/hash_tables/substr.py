# Substring equality

def precompute_hashes(string: str):
    n = len(string)
    hashes1 = [0]
    hashes2 = [0]

    for i in range(n):

        h1 = (hashes1[i] * x + ord(string[i])) % p1
        h2 = (hashes2[i] * x + ord(string[i])) % p2
        hashes1.append(h1)
        hashes2.append(h2)

    return hashes1, hashes2


def equality(a, b, l):

    x_l_p1 = pow(x, l, p1) # x**l
    x_l_p2 = pow(x, l, p2)

    hash_a_1 = (hashes1[a+l] - hashes1[a] * x_l_p1) % p1
    hash_a_2 = (hashes2[a+l] - hashes2[a] * x_l_p2) % p2

    hash_b_1 = (hashes1[b+l] - hashes1[b] * x_l_p1) % p1
    hash_b_2 = (hashes2[b+l] - hashes2[b] * x_l_p2) % p2
    
    if hash_a_1 == hash_b_1 and hash_a_2 == hash_b_2:
        print('Yes')
        return  
    print('No') 


if __name__ == "__main__":
    string = input()
    n = int(input())

    queries = []
    for _ in range(n):
        q = list(map(int, input().split(' ')))
        queries.append(q)

    x = 256
    p1 = 10 ** 9 + 7
    p2 = 10 ** 9 + 9
    hashes1, hashes2 = precompute_hashes(string)

    for a, b, l in queries:
        equality(a, b, l)
