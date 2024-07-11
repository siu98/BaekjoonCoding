#백준9465: 스티커
import sys 
input = sys.stdin.readline

T = int(input())
sticker = []
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)] 
    
    dp = [[0]*n for _ in range(2)]

    #스티커 길이가 1일 때
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    #스티커의 길이가 2 일떼
    dp[0][1] = sticker[1][0] + sticker[0][1]
    dp[1][1] = sticker[0][0] + sticker[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    #스티커의 길이가 3개 이상일 때 
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + sticker[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + sticker[1][i]
        continue 

    print(max(dp[0][-1],  dp[1][-1]))