# 1 2 3 1 이 순서대로 들어와야 한다.
# 하나씩 새로운 리스트에 넣으면서 만약 맨 뒤에서 부터 1 2 3 1이 나오게 되면 개수 + 1 및 
# pop을 사용해서 지워준다.

def solution(ingredient):
    answer = 0
    hamburger = []
    for i in ingredient:
        hamburger.append(i)
        if hamburger[-4:] == [1, 2, 3, 1]:
            answer += 1
            for j in range(4):
                hamburger.pop()   
    return answer