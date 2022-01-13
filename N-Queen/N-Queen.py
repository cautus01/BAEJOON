import sys
input=sys.stdin.readline
n=int(input())
v1=[0]*n
v2=[0]*50
v3=[0]*50
count=0

def func(k):
    global count
    if k==n:
        count+=1
        return
    for i in range(n):
        if v1[i]==1 or v2[i+k]==1 or v3[i-k+n-1]==1:
            continue
        v1[i]=1
        v2[i+k]=1
        v3[i-k+n-1]=1
        func(k+1)
        v1[i] = 0
        v2[i+k] = 0
        v3[i-k+n-1] = 0
func(0)
print(count)