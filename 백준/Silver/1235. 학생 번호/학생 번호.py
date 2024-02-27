#백준1235 : 학생 번호
N = int(input())
student = []
for _ in range(N):
    student.append(str(input()))
for i in range(1, len(student[0])+1):
    res = []
    for j in range(N):
        if student[j][-i:] in res:
            break
        else:
            res.append(student[j][-i:])
    if len(res) == N:
        print(i)
        break 