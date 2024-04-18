#벡준7785: 회사에 있는 사람
import sys
input = sys.stdin.readline

n = int(input())
number = dict()

for _ in range(n):
    x, y = map(str, input().split())
    
    if y == "enter":
        number[x] = y
    else:
        del number[x]
number = sorted(number.keys(), reverse=True)
for i in number:
    print(i)