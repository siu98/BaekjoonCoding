#백준 1026 : 보물
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort()

S = 0
for i in range(N):
    S += A[i]*B[i]
print(S)
