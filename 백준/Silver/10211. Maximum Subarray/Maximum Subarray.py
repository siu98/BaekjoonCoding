#백준10211: Maximum Subarray
import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    
    res = [X[0]]
    
    for i in range(1, N):
        big = max(res[i-1]+X[i], X[i])
        res.append(big)
    print(max(res))
        