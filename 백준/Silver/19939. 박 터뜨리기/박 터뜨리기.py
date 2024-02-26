#백준19939 : 박 터뜨리기
N, K = map(int, input().split())
ball = K*(K+1) //2
if N < ball:
    print(-1)
elif (N-ball) % K == 0:
    print(K-1)
else:
    print(K)