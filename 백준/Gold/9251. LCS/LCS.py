#백준9251: LCS
import sys 
input = sys.stdin.readline

sequence1 = list(input().strip())
sequence2 = list(input().strip())
dp = [[0]* (len(sequence2)+1) for _ in range(len(sequence1)+1)]

for i in range(1, len(sequence1)+1):
    for j in range(1, len(sequence2)+1):
        if sequence1[i-1] == sequence2[j-1]: 
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(sequence1)][len(sequence2)])
