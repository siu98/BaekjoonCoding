#백준11650 : 좌표 정렬하기
N=int(input())
list = []
for i in range(N):
    [x, y] = map(int, input().split())
    list.append([x, y])
list.sort()
for i in list:
    print(i[0], i[1])