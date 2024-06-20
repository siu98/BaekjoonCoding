#백준1388: 바닥 장식
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = []
visited = [[False]*M for _ in range(N)]
cnt = 0

for _ in range(N):
    array.append(list(input().strip()))

def dfs(x, y):
    visited[x][y] = True
    if array[x][y] == '|':
        if x + 1 < N and array[x + 1][y] == '|' and not visited[x + 1][y]:
            dfs(x + 1, y)
    elif array[x][y] == '-':
        if y + 1 < M and array[x][y + 1] == '-' and not visited[x][y + 1]:
            dfs(x, y + 1)

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

print(cnt)
