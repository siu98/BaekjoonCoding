def solution(a, b, n):
    answer = 0
    # 빈병이 많을 때만 
    while (n>=a):
        # remainCock: 바꾸지 않고 남아있는 콜라
        remainCock = n%a
        # 받은 콜라
        n = (n//a)*b 
        answer += n
        
        # 마지막에 남아있는 콜라 추가 해주기
        n += remainCock
    return answer