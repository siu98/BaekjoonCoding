#백준13417 : 카드 문자열
import sys
input = sys.stdin.readline
from collections import deque
 
for _ in range(int(input())):
    N = int(input())
    card = input().split()
    q = deque()
    q.append(card[0])
    st = card[0] # 기준
    
    for i in range(1, len(card)):
        if st >= card[i]:
            q.appendleft(card[i])
            st = card[i] # 기준은 매번 변하는 변수
        else:
            q.append(card[i])
            
    print(''.join(q))
