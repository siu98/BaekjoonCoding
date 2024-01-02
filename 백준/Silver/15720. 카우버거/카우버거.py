#백준 15720 : 카우버거
B, C, D = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

res = 0
minValue = min(B, C, D)
for i in range(minValue):
    res += (burger[i]+side[i]+drink[i])*0.9
res += sum(burger[minValue::])
res += sum(side[minValue::])
res += sum(drink[minValue::])
print(sum(burger)+sum(side)+sum(drink))
print(int(res))