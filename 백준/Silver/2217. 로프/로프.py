#백준 2217 : 로프
N = int(input())
list = []
for i in range(N):
    list.append(int(input()))
list.sort(reverse=True)    
res = []
for j in range(N):
    res.append(list[j]*(j+1))
print(max(res))