#백준 1654 : 랜선 자르기
N, K = map(int, input().split())
lan = []
for _ in range(N):
    lan.append(int(input()))
small = 1
large = max(lan)
while small <= large:
    mid = (small + large)//2
    num = 0
    for i in lan:
        num += i//mid
    if num >= K:
        small = mid + 1
    else:
        large = mid - 1
print(large)