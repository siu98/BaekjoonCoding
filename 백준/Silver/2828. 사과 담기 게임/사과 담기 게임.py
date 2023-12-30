#백준 2828 : 사과 담기 게임
N, M = map(int, input().split())
j = int(input())

left = 1
right = M
cnt = 0

for _ in range(j):
    apple = int(input())
    if left <= apple and right >= apple:
        continue
    elif left > apple:
        cnt += (left - apple)
        right -= (left - apple)
        left = apple
    else:
        cnt += (apple - right)
        left += (apple - right)
        right = apple
print(cnt)