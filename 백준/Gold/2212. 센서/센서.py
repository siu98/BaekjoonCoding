#백준 2122 : 센서
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
pos = sorted(list(map(int, sys.stdin.readline().split())))

if K >= N:
    print(0)
    sys.exit()

dist = []
for i in range(1, N):
    dist.append(pos[i] - pos[i-1])

dist.sort(reverse=True)
for _ in range(K-1):
    dist.pop(0)

print(sum(dist))