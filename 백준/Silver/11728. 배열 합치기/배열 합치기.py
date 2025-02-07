#백준11728: 배열합치기
import sys
input = sys.stdin.readline

N, M = map(int, (input().split()))
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arr = sorted(arrA+arrB)
print(*arr, sep=' ')