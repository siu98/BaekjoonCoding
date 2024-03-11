#백준15553: 난로
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
hour = []
for _ in range(N):
    hour.append(int(input())) #친구 도착시간
fireplace = []
for i in range(N-1):
    fireplace.append(hour[i+1] - hour[i])
fireplace.sort()
for _ in range(K-1):
    fireplace.pop()
for i in range(K):
    fireplace.append(1)
#print(fireplace) 
print(sum(fireplace))