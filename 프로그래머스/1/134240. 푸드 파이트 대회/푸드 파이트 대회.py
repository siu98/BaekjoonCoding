# 가운데 0을 기준으로 양쪽에 더해주기
def solution(food):
    tmp = ''
    for i in range(1, len(food)):
        tmp += str(i) *(food[i]//2)
        
    return tmp + '0' + tmp[::-1]