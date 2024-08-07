def solution(nums):
    Pokemon = len(set(nums))
    
    if len(nums)/2 > Pokemon:
        return Pokemon
    else:
        return len(nums)/2


#우선 겹치는 번호가 있으면 안되니까 set 사용 
#만약 set을 사용했을 때 개수가 nums/2 의 개수보다 작으면 set의 개수가 답
#nums/2의 개수가 더 크면 nums/2가 답    