#백준1059: 좋은구간
import sys
input = sys.stdin.readline
L = int(input())  #집합의 크기
setList = list(map(int, input().split()))
n = int(input())
setList.sort()
if n in setList:
    print(0)
else:
    max = 0
    min = 0
    for num in setList:
        if num < n:
            min = num
        elif num >n and max == 0:
            max = num
    max -= 1
    min += 1
    print((n-min)*(max-n+1)+(max-n))
        
