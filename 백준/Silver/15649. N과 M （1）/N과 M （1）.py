#백준15649: N과 M(1)
import sys
from itertools import permutations
input = sys.stdin.readline
N, M = map(int, input().split())
numList = [ i for i in range(1, N+1)]
for i in permutations(numList, M):
    print(*i)