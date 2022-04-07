import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[0]*m
isused=[0]*(n+1)
def func(k):
    if k==m:
        print(*arr)
        return
    else:
        for i in range(1,n+1):
            if isused[i]==0:
                arr[k]=i
                isused[i]=1
                for j in range(i):
                    isused[j]=1
                func(k+1)
                isused[i]=0
                for j in range(i):
                    isused[j]=0
func(0)
