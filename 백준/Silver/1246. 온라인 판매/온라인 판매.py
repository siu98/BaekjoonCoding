#백준1246: 온라인 판매
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
P = [int(input()) for _ in range(M)]
P.sort() 
res = 0 
target = 0 
for i in range(M):
    egg = min(M - i, N) 

   
    if res < P[i] * egg:
        res = P[i] * egg 
        target = P[i] 

print(target, res)