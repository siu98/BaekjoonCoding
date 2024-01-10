#백준 1018번 : 체스판 다시 칠하기
n, m = map(int, input().split())
chess = [] #체스판 저장 
res = [] #결과값 저장 

#input함수를 chess로 
for _ in range(n):
    chess.append(input())

#이중 for문사용 -> 8^8이기 때문에 -7을 사용함
for i in range(n-7):
    for j in range(m-7):
        #시작하는 판 색이 검정이거나 흰색
        black = 0
        white = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 ==0:
                    if chess[k][l] != 'B':
                        white+= 1
                    if chess[k][l] != 'W':
                        black+= 1
                else:
                    if chess[k][l] != 'W':
                        white+= 1
                    if chess[k][l] != 'B':
                        black+= 1
        res.append(black)
        res.append(white)
 
print(min(res))