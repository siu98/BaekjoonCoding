#백준 1789 : 수들의 합
N=int(input())
sum=0
res=0
for i in range(1, N+1):
  sum += i
  res += 1
  if sum > N:
    res -= 1
    break
print(res)