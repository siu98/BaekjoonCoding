#백준15686: 치킨 배달
import sys
from itertools import combinations 
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
res = float('inf')
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i ,j])
        elif city[i][j] == 2:
            chicken.append([i ,j])
for k in combinations(chicken, M): #조합: N개 중 M개 선택
    #치킨 거리 구하기
    CityDistance = 0
    for home in house:
        distance = float('inf')
        for j in range(M):
            distance = min(distance, abs(home[0]-k[j][0]) + abs(home[1]-k[j][1]))
        CityDistance += distance
    res = min(res, CityDistance)
print(res)    