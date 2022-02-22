import math
import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())

answer=n
for i in a:
    if i>b:
        answer+=math.ceil((i-b)/c)
print(answer)