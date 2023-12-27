#백준 1448 : 삼각형 만들기
import sys

N = int(input())
straw = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse = True)
res = -1

for i in range(N-2):
    if straw[i] < straw[i+1] + straw[i+2]:
        res = straw[i] + straw[i+1] + straw[i+2]
        break
print(res)