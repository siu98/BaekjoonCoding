#백준 2156 : 포도주 시식
n = int(input())
wine = [0]*10000
for i in range(n):
  wine[i] = int(input())

dp = [0]*10000
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[2] + wine[0], wine[2] + wine[1], dp[1])
for i in range(3,n):
  dp[i] = max(wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3], dp[i-1])

print(max(dp))