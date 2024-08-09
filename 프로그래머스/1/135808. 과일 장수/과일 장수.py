# 내림차순 정렬
# m 개씩 끊어서 보기
def solution(k, m, score):
    maxProfit = 0
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):
        fruit = score[i:i+m]
        
        if len(fruit) == m:
            maxProfit += min(fruit) * m 
    return maxProfit

