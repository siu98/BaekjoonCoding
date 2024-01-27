#백준 1004 : 어린왕자
T = int(input())
for _ in range(T):
    cnt = 0
    X1, Y1, X2, Y2 = map(int, input().split())
    n = int(input()) #행성의 개수
    for i in range(n):
        Cx, Cy, r = map(int, input().split())
        distance1 = (X1-Cx)**2 + (Y1-Cy)**2
        distance2 = (X2-Cx)**2 + (Y2-Cy)**2
        if (distance1 < r**2 and distance2 > r**2) or (distance1 > r**2 and distance2 < r**2):
            cnt +=1
    print(cnt)