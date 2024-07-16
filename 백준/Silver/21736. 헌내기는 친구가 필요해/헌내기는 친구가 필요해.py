#백준21736: 헌내기는 친구가 필요해
#bfs 사용하기  -> deque 사용 
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
campus = []

q = deque()
for i in range(N):
    row = list(input().rstrip())
    for j in range(M):
        if row[j] == 'I':
            q.append((i, j))
    campus.append(row)

visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


cnt = 0
    #우선 배열 안에 들어오는지 부터 검사 
while q:
    x, y = q.popleft()
    for direction in range(4):
        nx = dx[direction] + x
        ny = dy[direction] + y 
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if campus[nx][ny] != 'X':
                visited[nx][ny] = True  #방문 표시 하기
                q.append((nx, ny))
                if campus[nx][ny] == 'P':
                    cnt += 1

if cnt > 0:
    print(cnt)

else:
    print("TT")