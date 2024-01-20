#백준 1003 : 피보나치 함수
T = int(input())
zero = [1,0,1]
one = [0,1,1]

def fibo(N) : 
    if len(zero) <=N :
        for i in range(len(zero), N+1) :
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[N],one[N])

for i in range(T) : 
    a = int(input()) 
    fibo(a)