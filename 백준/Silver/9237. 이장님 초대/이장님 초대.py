#백준 9237 : 이장님 초대
N = int(input())
tree = list(map(int, input().split()))
tree.sort(reverse=True) #내림차순 정렬
day = []
for i in range(N):
    day.append(tree[i] + i + 1) 
print(max(day)+1)