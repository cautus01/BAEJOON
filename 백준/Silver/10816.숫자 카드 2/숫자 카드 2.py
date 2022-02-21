from collections import Counter
import sys
input=sys.stdin.readline
n=int(input())
card=list(map(int,input().split()))
counter=Counter(card)
m=int(input())
m_list=list(map(int,input().split()))
data=[]
for i in range(m):
    data.append(counter[m_list[i]])
print(*data,end=' ')