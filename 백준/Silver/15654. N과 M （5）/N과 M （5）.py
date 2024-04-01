#백준 15654: N과 M(5)
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
res = list(permutations(numList, M))
for i in range(len(res)):
    for j in range(M):
        print(res[i][j], end=" ")
    print()