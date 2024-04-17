#백준11651: 좌표 정렬하기2
import sys
input = sys.stdin.readline
N = int(input())
array = []
for i in range(N):
    x, y = map(int, input().split())
    array.append([y, x])
sortedArray = sorted(array)
for y, x in sortedArray:
    print(x, y)