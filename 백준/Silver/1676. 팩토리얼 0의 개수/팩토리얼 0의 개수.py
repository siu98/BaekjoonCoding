#백준1676: 팩토리얼 0의 개수
import sys
input = sys.stdin.readline
def factorial(N):
    num = 1
    for i in range(1, N+1):
        num *= i
    return num
cnt = 0
N = int(input())
fac = factorial(N)
fac_str = str(fac)
for i in range(len(fac_str)-1, -1, -1):
    if fac_str[i] == '0':
        cnt += 1
    else:
        break
print(cnt)