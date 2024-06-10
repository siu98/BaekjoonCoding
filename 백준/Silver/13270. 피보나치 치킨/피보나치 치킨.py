#백준13270: 피보나치 치킨
import sys
input = sys.stdin.readline
MXN = 10000
dp = [[0, 0] for _ in range(MXN + 1)]
a, b = 1, 2

n = int(input())

for i in range(1, n + 1):
    dp[i][0] = 1e9

while b <= n:
    for i in range(b, n + 1):
        dp[i][0] = min(dp[i][0], dp[i - b][0] + a)
        dp[i][1] = max(dp[i][1], dp[i - b][1] + a)
    b, a = b + a, b

print(dp[n][0], dp[n][1])
