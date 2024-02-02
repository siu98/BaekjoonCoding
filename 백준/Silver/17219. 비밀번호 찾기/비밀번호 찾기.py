#백준17219 : 비밀번호 찾기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for _ in range(N):
    site, password = input().split()
    dic[site] = password

for _ in range(M):
    print(dic[input().rstrip()])