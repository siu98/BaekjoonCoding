#백준1027: 고층 건물
import sys
input = sys.stdin.readline
N = int(input())
building = list(map(int, input().split()))
res = [0]*N

for i in range(N-1):
    Maxangle = -float('inf')    
    for j in range(i+1, N):
        angle = (building[j] - building[i]) /(j-i)
        if angle <= Maxangle:
            continue
        Maxangle = max(Maxangle, angle)
        res[i]+=1
        res[j]+=1
print(max(res))