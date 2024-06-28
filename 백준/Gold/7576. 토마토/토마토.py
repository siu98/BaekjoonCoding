#백준7576: 토마토
#bfs???
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])            
res = 0 

def bfs():
    while queue: #남아 있으면 돌리기
        x, y = queue.popleft() #첫 토마토 꺼내기
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])

bfs()

for i in tomato:
    for a in i:
        if a == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)
