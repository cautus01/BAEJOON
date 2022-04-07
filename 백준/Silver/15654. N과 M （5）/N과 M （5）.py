import sys
input=sys.stdin.readline

n,m=map(int,input().split())
data=sorted(list(map(int,input().split())))
arr=[]
isused=[0]*(n+1)
def func(k):
    if k==m:
        print(*arr)
        return
    else:
        for i in range(n):
            if isused[i]==0:
                isused[i]=1
                arr.append(data[i])
                func(k+1)
                arr.pop()
                isused[i]=0
func(0)