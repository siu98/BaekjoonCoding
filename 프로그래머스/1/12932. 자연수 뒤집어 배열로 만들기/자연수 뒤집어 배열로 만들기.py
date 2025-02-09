def solution(n):
    # n을 문자열로 바꾼 후 각 문자를 정수로 변환 
    answer = list(map(int, str(n)))  
    return answer[::-1]