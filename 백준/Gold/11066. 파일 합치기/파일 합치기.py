import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    sum=[[0]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            sum[i][j]=sum[i][j-1]+arr[j]
    d=[[int(1e9)]*n for _ in range(n)]
    for i in range(n):
        d[i][i]=0
    for len in range(1,n):
        for i in range(0,n-len):
            j=i+len
            for k in range(i,j):
                d[i][j]=min(d[i][j],d[i][k]+d[k+1][j]+sum[i][j])
    print(d[0][n-1])
