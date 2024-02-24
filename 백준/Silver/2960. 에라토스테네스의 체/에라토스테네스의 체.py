#백준2960: 에라토스테네스의 체
N, K = map(int, input().split())
cnt = 0
P = [True]*(N+1)
for i in range(2, N+1):
    for j in range(i, N+1, i):
        if P[j] != False:
            P[j] = False
            cnt += 1
            if cnt == K:
                print(j)