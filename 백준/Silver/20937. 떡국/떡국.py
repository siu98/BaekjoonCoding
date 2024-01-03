#백준 20937 : 떡국
n = int(input())
list = list(map(int, input().split()))
res = 1
list.sort(reverse=True)
cnt = 1
for i in range(len(list)-1):
    if list[i] == list[i+1]:
        cnt += 1
        res = max(res, cnt)
    else:
        cnt = 1
print(res)