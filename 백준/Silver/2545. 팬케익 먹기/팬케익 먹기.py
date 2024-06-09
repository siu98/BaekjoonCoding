#백준2545: 팬케익 먹기
T = int(input())
result = []
for _ in range(T):
    input()
    A, B, C, D = map(int, input().split())
    A, B, C = sorted((A, B, C))
    sum = A + B + C - D
    tmp = min(sum // 3, A)
    A1 = tmp
    sum -= tmp
    tmp = min(sum // 2, B)
    print(A1*tmp*(sum-tmp))