#백준1193 : 분수찾기
X = int(input())
line = 1
while X>line:
    X-=line
    line+=1
if line%2==0:
    x = X
    y = line - X + 1
else:
    x = line - X + 1
    y = X
print(x, '/', y, sep='')