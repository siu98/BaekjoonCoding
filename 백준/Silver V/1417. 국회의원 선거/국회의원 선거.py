#백준1417 : 국회의원 선거
N = int(input())
candi = []
cnt = 0
for i in range(N):
    M = int(input())
    candi.append(M)
#print(candi)
while True:
    if (candi[0] == max(candi) and candi.count(max(candi)) == 1):
        break
    j = candi.index(max(candi), 1, N)
    candi[j] -= 1
    candi[0] += 1
    cnt += 1
print(cnt)