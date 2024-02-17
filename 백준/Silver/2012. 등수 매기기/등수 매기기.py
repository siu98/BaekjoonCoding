#백준2012 : 등수 매기기
import sys
N = int(sys.stdin.readline())
grade = []
for _ in range(N):
    grade.append(int(sys.stdin.readline()))
grade.sort()
res = 0
for i in range(1,  N+1):
    res += abs(i-grade[i-1])
print(res)