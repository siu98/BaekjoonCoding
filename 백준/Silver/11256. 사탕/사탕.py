#백준 11256 : 사탕
T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    
    candy = []
    for _ in range(N):
        length, width = map(int, input().split())
        candy.append(width*length)
    candy.sort(reverse=True)
    res = 0
    for i in range(len(candy)):
        J -= candy[i]
        res += 1
        if J <= 0:
            break
    print(res)