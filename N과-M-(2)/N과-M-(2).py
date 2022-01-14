n,m=map(int,input().split())
visited=[0]*(n+1) # 방문 여부
arr=[] # 숫자 넣기

def func(k):
    if k==m:
        for i in range(m):
            print(arr[i],end=' ')
        print()
        return
    for i in range(1,n+1):
        if visited[i]==0 and (arr==[] or arr[-1]<i):
            visited[i]=1
            arr.append(i)
            func(k+1)
            arr.pop()
            visited[i] = 0
func(0)