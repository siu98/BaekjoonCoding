#백준28353: 고양이 카페
N, K = map(int, input().split())
cat = list(map(int, input().split()))

cat.sort()
cnt = 0
left = 0
right = N - 1 
while left < right:
    if cat[left] + cat[right] <= K:
        cnt += 1
        left += 1
        right -= 1
    else:
        right -= 1
print(cnt)