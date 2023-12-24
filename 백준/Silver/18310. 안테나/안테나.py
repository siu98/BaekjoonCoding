#백준 18310 : 안테나
N = int(input())
antenna = list(map(int, input().split()))
antenna.sort()

if N % 2 == 0: #짝수일 때
    N = (N // 2) - 1
    print(antenna[N])
else:
    N = N // 2
    print(antenna[N]) 
    