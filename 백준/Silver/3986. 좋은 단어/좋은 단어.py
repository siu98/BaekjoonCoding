#백준3986: 좋은단어
import sys
input = sys.stdin.readline
N = int(input())
res = 0

for _ in range(N):
    stack = []
    _list = list(input().strip())
    for i in _list:
        if not len(stack):
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)

    if not len(stack):
        res += 1 

print(res)