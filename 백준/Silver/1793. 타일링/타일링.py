#백준1793 : 타일링
dp = [0 for i in range(251)]

while(True):
    try:
        N = int(input())
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3
        for i in range(3, N+1):
            dp[i] = dp[i-1] + 2*dp[i-2]
        print(dp[N])
    except:
        break