import sys

input = sys.stdin.readline
N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())
res = 0
for _ in range(M):
    t = input()
    if t in S:
        res+=1
print(res)