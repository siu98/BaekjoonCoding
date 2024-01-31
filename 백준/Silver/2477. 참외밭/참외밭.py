#백준 2477 : 참외밭
Kmelon = int(input())
width = []  #가로
height = [] #세로
total = []

for _ in range(6):
    dir, len = map(int, input().split())
    if dir == 1 or dir ==2:
        width.append(len)
        total.append(len)
    else:
        height.append(len)
        total.append(len)
maxArea = max(width)*max(height) #큰 직사각형
maxHeight = total.index(max(height))
maxWidth = total.index(max(width))

smallArea1 = abs(total[maxHeight-1]-total[(maxHeight-5 if maxHeight == 5 else maxHeight+1)])
smallArea2 = abs(total[maxWidth-1]-total[(maxWidth-5 if maxWidth == 5 else maxWidth+1)])

area = maxArea - (smallArea1*smallArea2)
print(area*Kmelon)