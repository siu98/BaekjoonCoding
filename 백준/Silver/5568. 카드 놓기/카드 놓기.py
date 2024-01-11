#백준 5568 : 카드 놓기
from itertools import permutations
n = int(input()) #n장의 카드
k = int(input()) #k장의 카드
card = []
for _ in range(n):
    c = input()
    card.append(c)
res = set() #집합생성 -> 중복제거 
for i in permutations(card, k): 
    res.add(''.join(i)) #join함수 -> 하나의 문자열로 합치기
print((len(res)))