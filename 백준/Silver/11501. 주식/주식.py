#백준11501 : 주식
T = int(input())
for i in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    profit = 0
    maxPrice = 0
    for j in range(len(price)-1, -1, -1):
        if price[j] > maxPrice:
            maxPrice = price[j]
        else:
            profit += maxPrice - price[j]
    print(profit)