import math

T = int(input(""))

for _ in range(T):
    N, M = map(int, input().split())
    bridge = math.factorial(M)//(math.factorial(M-N) * math.factorial(N))
    print(bridge)