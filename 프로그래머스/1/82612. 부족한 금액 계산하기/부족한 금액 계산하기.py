# price: 놀이기구 이용료
# money: 현재 가지고 있는 돈 
# count: 이용한 횟수
# for문을 사용해 이용한 횟수만큼 반복 + price*i 만큼 증가 
# money-sum >=0 이면 return 0  else이면 money-sum값 return

def solution(price, money, count):
    NewPrice = 0
    for i in range(count):
        NewPrice += price*(i+1)
    
    if money - NewPrice >= 0:
        return 0
    else:
        return abs(money - NewPrice)