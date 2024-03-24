#백준1015: 수열 정렬
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
sortedA = sorted(A, reverse=False)

P = []
for i in range(N):
    P.append(sortedA.index(A[i]))
    sortedA[sortedA.index(A[i])] = -1 
strP = [str(i) for i in P]
print(" ".join(strP))