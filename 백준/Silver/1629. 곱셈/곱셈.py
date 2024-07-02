#백준 1629: 곱셈
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def mul(A, B, C):
    if B == 1:
        return A%C
    elif B % 2 == 0:
        return (mul(A, B//2, C)**2)%C
    else:
        return ((mul(A, B//2, C)**2)*A)%C
print(mul(A, B, C))