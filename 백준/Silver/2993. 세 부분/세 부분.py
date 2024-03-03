#벡준2993: 세 부분
word = input()
res = word
for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        res = min(res, word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])
print(res)