#백준1912 :연속합
N = int(input())
arry = list(map(int, input().split()))
dp = [0]*N
dp[0] = arry[0]
for i in range(1, N):
    dp[i] = max(arry[i], dp[i-1]+arry[i])
print(max(dp))