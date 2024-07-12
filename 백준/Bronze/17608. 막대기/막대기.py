#백준17608: 막대기
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    stack.append(int(input()))

cnt = 1

for i in reversed(range(N)):
    if stack[i] > stack[-1]:
        cnt += 1
        stack[-1] = stack[i] 
print(cnt)