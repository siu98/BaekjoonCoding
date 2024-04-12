#백준1427: 소트인사이드
import sys
input = sys.stdin.readline
N = int(input())
num = []
for i in str(N):
    num.append(int(i))
num.sort(reverse=True)
 
for i in num:
    print(i,end='')