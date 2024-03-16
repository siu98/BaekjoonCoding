#백준4811: 알약
import sys
input = sys.stdin.readline

pill = [[0]*31 for _ in range(31)]
for i in range(1, 31):
    pill[0][i] = 1
for i in range(1, 31):
    for j in range(i, 31):
        pill[i][j] += pill[i-1][j] + pill[i][j-1]
while True:
    N = int(input())
    if N == 0:
        break

    print(pill[N][N])