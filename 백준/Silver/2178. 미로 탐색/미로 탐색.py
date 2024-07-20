# 백준2178: 미로 탐색
import sys
from collections import deque

input = sys.stdin.readline

# 방향 설정 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# bfs함수
def bfs(x, y):
    queue = deque([(x, y)])

    # 시작 위치 방문 표시
    visited[x][y] = True  

    while queue:
        x, y = queue.popleft()

        for i in range(4):

            # 현재위치에서 상하좌우로 이동한 새로운 위치
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

                # 새로운 위치의 거리를 현재위치의 거리에서 1을 더한 값으로 설정
                matrix[nx][ny] = matrix[x][y] + 1  

N, M = map(int, input().split())
matrix = []
visited = [[0] * M for _ in range(N)]

for _ in range(N):
    maze = list(map(int, input().strip()))
    matrix.append(maze)

#bfs 함수 호출
bfs(0, 0)       

print(matrix[N-1][M-1])
