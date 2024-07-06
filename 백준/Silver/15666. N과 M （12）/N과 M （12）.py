#백준:15666 : N과 M
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == M:
        print(*temp)
        return
    remember_me = 0
    for i in range(start, N):
        if remember_me != nums[i]:
            temp.append(nums[i])
            remember_me = nums[i]
            dfs(i)
            temp.pop()

dfs(0)