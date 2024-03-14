#16938: 캠프 준비
import sys
from itertools import combinations
input = sys.stdin.readline
N, L, R, X = map(int, input().split())
level = list(map(int, input().split()))
cnt = 0

for i in range(2, N+1):
    problem = combinations(level, i)
    for j in problem:
        if L <= sum(j) <= R and max(j)-min(j) >=X:
            cnt += 1
print(cnt)  