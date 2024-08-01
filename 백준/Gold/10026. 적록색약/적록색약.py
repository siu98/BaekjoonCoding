#백준10026: 적록색약
import sys
from collections import  deque
input = sys.stdin.readline

N = int(input())
q = deque()

color = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and color[nx][ny] == color[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

cnt1 = 0
for j in range(N):
    for k in range(N):
        if not visited[j][k]:
            bfs(j, k)
            cnt1 += 1

cnt2 = 0
for j in range(N):
    for k in range(N):
        if color[j][k] == 'G':
            color[j][k] = 'R'
   
          
visited = [[False] * N for _ in range(N)]
for j in range(N):
    for k in range(N):
        if not visited[j][k]:
            bfs(j, k)
            cnt2 += 1

print(cnt1, cnt2)