#백준 1049 : 기타줄

N, M = map(int, input().split())

packageSet = []
singleSet = []

for _ in range(M):
    package, single = input().split()
    packageSet.append(int(package))
    singleSet.append(int(single))


packageSet = min(packageSet)
singleSet = min(singleSet)

if packageSet < singleSet*6:
    if packageSet < (N%6)*singleSet:
        print((N//6)*packageSet+packageSet)
    else:
        print((N//6)*packageSet+ (N%6)*singleSet)
elif packageSet >= singleSet*6:
    print(N*singleSet)