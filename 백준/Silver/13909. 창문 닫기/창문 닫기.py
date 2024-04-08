#백준13909: 창문 닫기
import sys
input = sys.stdin.readline
N = int(input())
res = 0
window = 1
while window*window <= N:
    window += 1
    res +=1
print(res)