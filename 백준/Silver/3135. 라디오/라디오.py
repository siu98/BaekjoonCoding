#백준 3135 : 라디오
A, B = map(int, input().split())
res = abs(A-B)
for _ in range(int(input())):
    N = int(input())
    if res > abs(N-B):
        res = abs(N-B)+1
print(res)