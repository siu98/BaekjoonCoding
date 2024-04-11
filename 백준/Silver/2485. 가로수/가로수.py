#백준2485: 가로수
def gcd(m, n):
    while n != 0:
        t = m%n
        m = n
        n = t
    return abs(m)

N = int(input())
tree = []
distance = []
for i in range(N):
    tree.append(int(input()))
    if i != 0:
        distance.append(tree[i]-tree[i-1])

max_gcd = distance[0]
for i in range(N-2):
    max_gcd = gcd(distance[i+1]-distance[i], max_gcd)

result = ((tree[N-1]-tree[0])//max_gcd - 1) - N + 2 
print(result)