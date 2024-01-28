#백준 1181 : 단어 정렬
N = int(input())
word = []
for i in range(N):
    a = input()
    word.append(a)

word = list(set(word))
word = sorted(word, key = lambda x : (len(x), x))

for i in word:
    print(i)