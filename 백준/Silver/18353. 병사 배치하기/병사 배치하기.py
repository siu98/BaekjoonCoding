#백준18353 : 병사 배치하기
N = int(input())
soldier = list(map(int, input().split()))
dp = [1]*N
for i in range(N):
    for j in range(i):
        if soldier[j] > soldier[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))