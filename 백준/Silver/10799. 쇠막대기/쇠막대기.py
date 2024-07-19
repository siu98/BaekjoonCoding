#백준10799: 쇠막대기
import sys
input = sys.stdin.readline
stick = input()
stack = []
cnt = 0

for i in range(len(stick)):
    if stick[i] == "(":         # "("로 시작할 경우 stack에 넣기 
        stack.append(stick[i])
        # cnt += 1
    elif stick[i] == ")":       # 만약 ")" 일 경우 (레이저 인 경우)
        if stick[i-1] == "(":   # 1) 앞이 "(" 가 나올 때 pop으로 지우고 지우고 나머지 개수 만큼 cnt
            stack.pop()         # 레이저의 시작 부분인 "("를 제거        
            cnt += len(stack)
    
        else:                   # 레이저가 아닐 경우
            stack.pop()         # 막대기의 ")" 에 대응하는 앞 부분인 "("를 제거
            cnt += 1            # 1만 증가시키면 된다.
print(cnt)