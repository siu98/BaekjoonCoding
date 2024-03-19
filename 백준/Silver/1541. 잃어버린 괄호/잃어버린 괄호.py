#백준1541: 잃어버린 괄호
import sys
input = sys.stdin.readline
n = input().split('-')
num = []

for i in n:
    sum=0
    temp = i.split('+')
    for j in temp:
        sum += int(j)
    num.append(sum)
m = num[0]
for i in range(1, len(num)):
    m -= num[i]
print(m)