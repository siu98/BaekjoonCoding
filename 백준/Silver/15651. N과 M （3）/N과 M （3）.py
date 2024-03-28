#백준15651: N과 M(3)
import sys
from itertools import product
input = sys.stdin.readline
N, M = map(int, input().split())
numList = [ i for i in range(1, N+1)]
for i in product(numList, repeat=M):
    print(*i)