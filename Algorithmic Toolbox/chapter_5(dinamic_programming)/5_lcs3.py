# Longest Common Subsequence of Three Sequences Problem

def solve_problem(seq1: list, seq2: list, seq3: list) -> int:
    
    dp = [[[0] * (len(seq3) + 1) 
        for _ in range(len(seq2) + 1)] 
        for _ in range(len(seq1) + 1)]

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            for k in range(1, len(seq3) + 1):


                if seq1[i - 1] == seq2[j - 1] == seq3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    max_value = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
                    dp[i][j][k] = max_value

    return dp[-1][-1][-1]
    

if __name__ == "__main__":
    # seq1 = [8, 3, 2, 1, 7, 3]
    # seq2 = [8, 2, 1, 3, 8, 10, 7]
    # seq3 = [6, 8, 3, 1, 4, 7]

    n = int(input())
    seq1 = [int(i) for i in input().split(' ')]
    m = int(input())
    seq2 = [int(i) for i in input().split(' ')]
    k = int(input())
    seq3 = [int(i) for i in input().split(' ')]

    
    result = solve_problem(seq1, seq2, seq3)
    print(result)