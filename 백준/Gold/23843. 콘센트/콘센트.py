import sys
input = sys.stdin.readline
N, M = map(int, input().split())
hour = list(map(int, input().split()))
hour.sort(reverse=True) #내림차순 정렬

plug = [0]*M  #리스트 생성
socket = 0
for i in range(len(hour)):
    if socket == 0: #충전시간이 가장 긴 전자기기
        plug[socket] += hour[i]
        socket = (socket+1)%M
        continue
    plug[socket] += hour[i]
    if plug[socket] == plug[socket-1]:
        socket = (socket+1)%M
print(plug[0])