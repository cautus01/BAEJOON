import sys
input=sys.stdin.readline

n=int(input())
arr=[0]+list(map(int,input().split()))
d=[0]*(n+1)
for i in range(1,n+1):
    d[i]=max(0,d[i-1])+arr[i]
print(max(d[1:]))