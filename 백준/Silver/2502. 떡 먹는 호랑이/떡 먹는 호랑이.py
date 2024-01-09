#백준 2502 떡 먹는 호랑이

D, K = map(int, input().split()) #D->넘어온날 / K->떡의 개수

a, b = 1, 1 #a=1일차, b=2일차
for _ in range(4, D+1):
    a, b = b, a+b #a에 b, b에 a+b
a_cnt = 1 #첫날에 준 떡의 개수
b_cnt = 0 #둘 째날에 준 떡의 개수

while True:
    tmp = K - a*a_cnt # 현재까지 주어진 떡수 개수 빼기
    if tmp <0:
        break
    if tmp % b ==0: #tmp가 b의 배수이면 
        b_cnt = tmp//b
        break
    a_cnt +=1

print(a_cnt)
print(b_cnt)