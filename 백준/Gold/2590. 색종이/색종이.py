#백준2590: 색종이
import sys
input = sys.stdin.readline
paper = []
cnt = 0
for _ in range(6):
    paper.append(int(input()))
if paper[5]: #6x6 색종이 일 때
    cnt += paper[5]
while paper[4]: #5x5 색종이 일 때
    square = 11
    paper[4] -= 1
    paper[0] = max(paper[0]-11, 0)
    cnt += 1
while paper[3]: #4x4 색종이 일 떄
    square = 20
    square -= min(paper[1], 5)*4
    paper[3] -= 1
    paper[1] = max(paper[1]-5, 0)
    paper[0] = max(paper[0]-square, 0)
    cnt += 1 
while paper[2]: #3x3 색종이 일 때
    square = 36 - 9*min(paper[2], 4)
    if paper[2] >= 4:
        paper[2] -= 4
        square = 0
    elif paper[2] == 3:
        square -= min(1, paper[1])*4
        paper[2] -= 3
        paper[1] = max(paper[1]-1, 0)
    elif paper[2] == 2:
        square -= min(3, paper[1])*4 
        paper[2] -= 2
        paper[1] = max(paper[1]-3, 0)
    else:
        square -= min(5, paper[1])*4
        paper[2] -= 1
        paper[1] = max(paper[1]-5, 0) 
    paper[0] = max(paper[0]-square, 0)
    cnt += 1
while paper[1]:
    square = 36 - 4*min(paper[1], 9)
    paper[1] = max(paper[1]-9, 0)
    paper[0] = max(paper[0]-square, 0)
    cnt += 1
while paper[0]:
    paper[0] = max(paper[0]-36, 0)
    cnt += 1
print(cnt)    