#백준10815-1: 숫자카드
import sys
input = sys.stdin.readline

N = int(input().strip())        # 숫자 카드의 개수
# for _ in range(N):
card = set(map(int, input().split()))

res = []
M = int(input().strip())       # 구해야할 정수의 개수
# for _ in range(M):
isCard = list(map(int, input().split()))

for num in isCard:
    if num in card:
        res.append(1)
    else:
        res.append(0)

# for a in res:
#     print(a, end = " ")

print(' '.join(map(str, res)))