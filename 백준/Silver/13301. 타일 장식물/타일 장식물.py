#백준13301 : 타일 장식물
N = int(input())
tile = [0]*(N+2)
tile[1] = 1
for i in range(2, N+2):
    tile[i] = tile[i-1] + tile[i-2]
print((tile[N]+tile[N+1])*2)