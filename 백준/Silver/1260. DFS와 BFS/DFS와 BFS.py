#백준1260: DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline
N, M, V = map(int, input().split())
#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    V1, V2 = map(int, input().split())
    graph[V1][V2] = graph[V2][V1] = 1
#방문리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

def DFS(V): 
    visited1[V] = 1 #방문처리
    print(V, end = ' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            DFS(i)
def BFS(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0)
        print(V, end= ' ')
        for i in range(1, N+1):
            if visited2[i] == 0 and graph[V][i] == 1:
                queue.append(i)
                visited2[i] = 1 #방문처리
DFS(V)
print()
BFS(V)