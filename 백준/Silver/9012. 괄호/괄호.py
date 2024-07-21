#백준9012: 괄호
import sys
input = sys.stdin.readline

T= int(input())

for i in range(T):
    VPS = input()
    stack = []
    for j in VPS:

        # '(' 괄호가 들어있으면 스택에 넣는다.
        if j == '(':
            stack.append(j)

        # ')' 괄호가 나왔을 때 스택에 '('가 있으면 삭제하고, 없으면 'NO'를 출력 후 끝낸다.
        elif j == ')':
            if stack:
                stack.pop()
            else:       
                print('NO')
                break
    
    # 만약 모두 종료 후 스택에 아무것도 없으면 'YES'를 만약 '('가 남아있다면 'NO"를 출력한다.
    else:
        if not stack:
            print('YES')    
        else:
            print('NO')