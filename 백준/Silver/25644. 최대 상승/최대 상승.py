#백준25644: 최대 상승
N = int(input())
ANA = list(map(int, input().split()))
benefit = 0
res = 0
for i in range(N-1, -1, -1):
    benefit = max(benefit, ANA[i])
    res = max(benefit - ANA[i], res)
print(res)