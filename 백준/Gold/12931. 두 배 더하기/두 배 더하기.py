#백준 12931: 두 배 더하기
import sys
input = sys.stdin.readline
N = int(input())
B = list(int(x) for x in input().split())
B.sort()

cnt = 0
while sum(B) != 0:
    check = 0
    for i in range(N):
        if B[i] % 2 !=0 or B[i] == 0 or B[i] == 1:
            if B[i] == 0:
                continue
            else:
                B[i] -= 1
                cnt +=1
            check = 1
    if check == 0:
        for i in range(N):
            B[i]//=2
        cnt += 1
print(cnt)