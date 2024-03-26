#백준2805: 나무 자르기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)  #이진탐색에서 1부터 가장 큰 나무까지

while start <= end: #end보다 작거나 같을 동안 
    mid = (start + end) // 2 
    logSum = 0 
    for i in tree:
        if i>=mid:  #mid보다 더 크면 
            logSum += i-mid #i에서 mid 뺀 만큼
    if logSum >= M:
        start = mid + 1 #더 높이 잘라도 되기 때문
    else:
        end = mid -1 #작으면 하나 빼서 조정해봄
print(end)  