#백준1431: 시리얼 번호
import sys
input = sys.stdin.readline

guitar = []
for _ in range(int(input())):
    s = input().rstrip()
    
    summ = 0
    for i in s:
        if i.isdigit():
            summ += int(i)
    guitar.append((s,summ))
    
guitar.sort(key=lambda x:(len(x[0]),x[1],x[0]))

for i in guitar:
    print(i[0])