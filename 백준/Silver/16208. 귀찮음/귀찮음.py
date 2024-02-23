#백준16208 : 귀찮음
import sys
input = sys.stdin.readline

N = int(input())
stick = list(map(int, input().split()))
stick.sort()
total = sum(stick)
res = 0
for i in stick:
    res += i*(total-i)
    total -= i
print(res)