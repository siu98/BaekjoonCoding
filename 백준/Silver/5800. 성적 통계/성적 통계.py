#백준5800 : 성적 통계
K = int(input())
for i in range(K):
    N = list(map(int, input().split()))
    del N[0]
    N.sort()
    a = []
    print('Class', i+1)
    for i in range(len(N)-1):
        a.append(N[i+1]-N[i])
    print('Max', str(max(N))+',' ,'Min', str(min(N))+',', 'Largest gap', max(a))