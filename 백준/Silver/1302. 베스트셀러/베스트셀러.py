#백준1302 : 베스트셀러
import sys
input = sys.stdin.readline

N = int(input())
book = {}

for i in range(N):
    name = input()
    if name not in book:
        book[name] = 1
    else:
        book[name] += 1
maxValue = max(book.values())
bestSeller = []
for key, value in book.items():
    if value == maxValue:
        bestSeller.append(key)
bestSeller = sorted(bestSeller)
print(bestSeller[0])