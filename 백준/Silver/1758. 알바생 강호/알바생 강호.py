#백준1758: 알바생 강호 
N = int(input())
starbucks = []
for i in range(N):
    money = int(input())
    starbucks.append(money)
starbucks.sort(reverse=True)
sum = 0
for i in range(N):
    tips = starbucks[i] - i
    if tips < 0:
        break
    sum += tips
print(sum)