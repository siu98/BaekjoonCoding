#백준14469 : 소가 길을 건너간 이유
import sys
input = sys.stdin.readline

N = int(input())
cow =[]
for _ in range(N):
    cow.append(list(map(int, input().split())))
cow.sort(key=lambda x : (x[0], x[1]))
check = -1
for i in range(N):
    if cow[i][0] >= check:
        check = cow[i][0] + cow[i][1]
    else:
        check += cow[i][1]
print(check)