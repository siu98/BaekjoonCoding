#백준 2564 : 경비원
def cal_dist(loc, distance):
    if loc == 1: #북쪽
        return distance
    elif loc == 4: #동쪽
        return w+distance
    elif loc == 2: #남쪽
        return w+h+w-distance
    elif loc == 3: #서쪽
        return w+h+w+h-distance
w, h = map(int, input().split())

num = int(input())

location=[0]*(num+1) 

dist = []
for i in range(num+1):
    loc, distance = map(int, input().split())
    dist.append(cal_dist(loc, distance))

dong_dist = dist[-1]
ans = 0
for i in range(num):
    cal_distance = abs(dist[i]-dong_dist)
    total = 2*(w+h)
    ans+= min(cal_distance, total-cal_distance)
print(ans)