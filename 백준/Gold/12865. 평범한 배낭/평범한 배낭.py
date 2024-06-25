#백준12865: 평범한 배낭
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
knapsack = []
for i in range(N):
    W, V = list(map(int, input().split()))
    knapsack.append((W, V))
dp = [0]*(K+1)

for W, V in knapsack:
    for j in range(K, W - 1, -1):
        dp[j] = max(dp[j], dp[j - W] + V)

print(dp[K])
