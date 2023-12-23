#백준 1449 : 수리공 항승

N, L = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()

tape = 1
distance = 0
for i in range(1, N):
    distance += abs(leak[i]-leak[i-1])
    if L > distance:
        continue
    else:
        tape +=1
        distance = 0
print(tape)