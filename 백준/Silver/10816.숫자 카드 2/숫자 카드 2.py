from collections import Counter
import sys
input=sys.stdin.readline
n=int(input())
card=list(map(int,input().split()))
counter=Counter(card)
m=int(input())
m_list=list(map(int,input().split()))
for i in range(m):
    print(counter[m_list[i]],end=' ')