#백준10845: 큐
import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    order = input().split()

    if order[0] == 'push':
        queue.insert(0, order[1])
    elif order[0] == 'pop':
        if len(queue) != 0:
            print(queue.pop())  
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) != 0:
            print(0)
        else: 
            print(1)
    elif order[0] == 'front':
        if len(queue) != 0:
            print(queue[-1])
        else: 
            print(-1)
    elif order[0] == 'back':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)