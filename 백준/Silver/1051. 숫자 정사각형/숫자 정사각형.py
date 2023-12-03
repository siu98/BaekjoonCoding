N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(input()))
x = min(N,M)#가로와 세로중 더 짧은 쪽 고르기 -> 한 변이 짧은 쪽을 넘기 힘들다
ans = 0
for i in range(N):
    for j in range(M):
        for k in range(x):
            if ((i+k)<N) and ((j+k)<M) and (arr[i][j] == arr[i][j+k] == arr[i+k][j] ==arr[i+k][j+k]):
                ans = max(ans, (k+1)**2)

print(ans)