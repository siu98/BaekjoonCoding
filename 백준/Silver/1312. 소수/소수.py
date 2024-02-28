#벡준1312 : 소수
A, B, N = map(int, input().split())
for i in range(N):
    A = (A%B)*10
    res = A//B
print(res)