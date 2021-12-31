from collections import deque
n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
num=1
arr=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(i,j,num):
    q=deque()
    q.append((i,j))
    graph[i][j]=num
    data=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]!=1:
                continue
            if graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny]=num
                data+=1
    arr.append(data)
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            num+=1
            bfs(i,j,num)
print(num-1)
arr.sort()
for i in range(len(arr)):
    print(arr[i])