#백준1764 : 듣보잡
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = [input().rstrip() for _ in range(N)]
see = [input().rstrip() for _ in range(M)]

res = list(set(listen) & set(see))

res.sort()
print(len(res))
for a in res:
    print(a)