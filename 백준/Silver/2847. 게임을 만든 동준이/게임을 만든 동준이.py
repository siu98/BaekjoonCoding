#백준2847 : 게임을 만든 동준이
N = int(input())
score = []
for i in range(N):
    score.append(int(input()))
cnt = 0
for i in range(N-2, -1, -1):
    if score[i] >= score[i+1]:
        cnt += score[i] - score[i+1] + 1
        score[i] = score[i+1] - 1
print(cnt)