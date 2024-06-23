#백준15663: N과 M (9)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False]*N
temp = []

def dfs():
    check = 0
    if len(temp) == M:
        print(*temp)
    for i in range(N):
        if check != num[i] and visited[i] == 0:
            temp.append(num[i])
            visited[i] = 1
            check = num[i]
            dfs()
            temp.pop()
            visited[i] = 0
dfs()