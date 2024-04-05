#백준 15656: N과 M(7)
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
res = list(combinations_with_replacement(numList, M))
for i in range(len(res)):
    for j in range(M):
        print(res[i][j], end=" ")
    print()