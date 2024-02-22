#백준20115 : 에너지 드링크
N = int(input())
drink = list(map(int, input().split()))
drink.sort()

sum = drink[-1]
for i in range(N-1):
    sum += drink[i]/2
print(sum)