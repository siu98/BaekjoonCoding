#백준10866 : 덱
from collections import deque
import sys
input = sys.stdin.readline

d = deque()
N = int(input())

for _ in range(N):
    deck = input().split()

    if deck[0] == 'push_front':
        d.appendleft(deck[1])
    
    elif deck[0] == 'push_back':
        d.append(deck[1])

    elif deck[0] == 'pop_front':
        if d:
            print(d[0])
            d.popleft()
        else:
            print(-1)
    
    elif deck[0] == 'pop_back':
        if d:
            print(d[-1])
            d.pop()
        else: 
            print(-1)
    
    elif deck[0] == 'size':
        print(len(d))
    
    elif deck[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    
    elif deck[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)

    elif deck[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)
        