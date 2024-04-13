#백준1735: 분수 합
import sys
input = sys.stdin.readline
def gcd(x,y): 
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y    
A, B = map(int, input().split())
C, D = map(int, input().split())
N = gcd(A*D + C*B, B*D) 
print((A*D + C*B)//N, B*D//N)