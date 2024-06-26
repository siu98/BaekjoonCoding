#백준4963: 섬의 개수
#dfs 사용하면 될 듯?
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def dfs(x, y):
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [1, 0, -1, 1, -1, 0, 1, -1]
    
    island[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1:
            dfs(nx, ny)
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = []
    cnt = 0
    for _ in range(h):
        island.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)