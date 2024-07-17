#백준2164: 카드2
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

# cards = [i for i in range(1, N + 1)]
cards = deque(range(1, N+1))
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft()) 
print(cards[0])