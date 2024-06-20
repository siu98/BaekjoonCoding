import sys
input = sys.stdin.readline

alphaHint = [3, 2, 1, 2, 3, 
             3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2,
             1, 2, 1, 1, 1, 2, 2, 1]

A = input().strip()
B = input().strip()

alpha = []
for i in range(len(A)):
    alpha.append(alphaHint[ord(A[i])-65])
    alpha.append(alphaHint[ord(B[i])-65])

while len(alpha) != 2:
    temp = []
    for j in range(len(alpha) - 1):
        temp.append((alpha[j] + alpha[j+1]) % 10)
    alpha = temp

print(f"{alpha[0]}{alpha[1]}")
