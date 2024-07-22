#백준11478: 서로 다른 부분 문자열의 개수
import sys
input = sys.stdin.readline

S = input().strip()
cnt = []

# 리스트에서 0부터 i-1까지 돌기 그 후 슬라이싱 i 부터
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        cnt.append(S[i:j])

print(len(set(cnt)))