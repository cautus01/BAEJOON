n,m=map(int,input().split())
isused=[False]*(n+1)
arr=[]

def func(k):
    if k==m:
        for i in range(m):
            print(arr[i],end=' ')
        print()
        return
    for i in range(1,n+1):
        if isused[i]!=True:
            arr.append(i)
            isused[i]=True
            func(k+1)
            isused[i]=False
            arr.pop()
func(0)