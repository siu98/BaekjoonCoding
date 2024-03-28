#백준15652: N과 M(4)
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
N, M = map(int, input().split())
numList = [ i for i in range(1, N+1)]
for i in combinations_with_replacement(numList ,M):
    print(*i)