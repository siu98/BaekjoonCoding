#백준28278: 스택 2
import sys
input = sys.stdin.readline
N = int(input())
stack = [] 
for _ in range(N):
    X = input().split()
    if X[0] == '1':
        stack.append(X[1])
    elif X[0] == '2':
        if stack:
            print(stack.pop())
        else: 
            print(-1)
    elif X[0] == '3':
        print(len(stack))
    elif X[0] == '4':
        if stack:
            print(0)
        else: 
            print(1)
    elif X[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)