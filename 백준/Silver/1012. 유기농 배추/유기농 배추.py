import sys
from collections import deque

input = sys.stdin.readline

# 방향 설정 (상, 하, 좌, 우)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    matrix[x][y] = 0  # 방문한 곳은 0으로 설정
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0  # 방문한 곳은 0으로 설정

T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1
    
    cnt = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
