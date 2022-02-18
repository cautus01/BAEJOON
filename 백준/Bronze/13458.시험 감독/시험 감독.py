import math
import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
dp=[0]*1000005
answer=0
for i in a:
    if i<=b:
        answer+=1
    else:
        answer=answer+1+math.ceil((i-b)/c)
print(answer)
