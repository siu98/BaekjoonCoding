# 1. 오름차순 정렬
# 1 2 2 3 3 4 5 5 -> 중복되는 수가 가장 많은 경우 부터 k개 세기
# ex) 위의 크기에서 k = 6 일 때, 배열 안에서 겹치는 수가 가장 큰 것 부터 세기 
# 딕셔너리를 사용하여 key(귤 크기) -value(개수)
def solution(k, tangerine):
    tangerineBox = {}  # 딕셔너리 생성
    
    for tanger in list(set(tangerine)):
        tangerineBox[tanger] = 0
        
    for tanger in tangerine:
        tangerineBox[tanger] += 1
        
    # value 값 기준으로 내림차순
    sortedTangerineBox = sorted(tangerineBox.items(), key=lambda x:x[1], reverse=True)
    answer = 0
    cnt = 0
    for i in sortedTangerineBox:

        if cnt + i[1] < k:
            cnt += i[1]
            answer += 1
            # return answer
        else:
            return answer + 1
