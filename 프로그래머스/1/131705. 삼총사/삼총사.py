# 조합을 사용하여 3개를 택한 후 원소의 합이 0 일 경우만 cnt 하기 
from itertools import combinations
def solution(number):
    answer = 0
    for number in combinations(number, 3):
        if sum(number) == 0:
            answer += 1
    return answer