#백준 2108 : 통계학
import sys
input=sys.stdin.readline

N=int(input())
arry=[]

for i in range(N):
    arry.append(int(input()))

arry.sort()
print(round(sum(arry)/len(arry)))
print(arry[len(arry)//2])

dic=dict()
for i in arry:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
mx=max(dic.values())
mx_dic=[]

for i in dic:
    if mx==dic[i]:
        mx_dic.append(i)

if len(mx_dic)>1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
    
print(max(arry)-min(arry))