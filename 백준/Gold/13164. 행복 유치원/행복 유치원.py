#백준13164: 행복 유치원
import sys 
input = sys.stdin.readline  
N, K = map(int, input().split())
height = list(map(int, input().split()))
price = []
for i in range(1, N):
    price.append(height[i]-height[i-1])
price.sort(reverse=True)
print(sum(price[K-1:]))