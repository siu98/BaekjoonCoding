#백준1064 : 평행사변형
ax, ay, bx, by, cx, cy = map(int, input().split())
#평행사변형이 나오지 않을 때 = 기울기가 같을 떄
if (cx-bx)*(by-ay) == (bx-ax)*(cy-by): 
    print(-1.0)
    exit(0)
#각각 선분의 길이 구하기
ab_length = ((ax-bx)**2 + (ay-by)**2)**0.5
bc_length = ((bx-cx)**2 + (by-cy)**2)**0.5
ca_length = ((cx-ax)**2 + (cy-ay)**2)**0.5
circum = [(ab_length + bc_length)*2, (bc_length + ca_length)*2, (ca_length + ab_length)*2]
res = max(circum) - min(circum)
print(res)