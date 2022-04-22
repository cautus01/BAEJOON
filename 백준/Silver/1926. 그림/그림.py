from collections import deque

n,m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))
max_value=0  
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    w=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
                
            if graph[nx][ny]==0:
                continue
                
            if graph[nx][ny]==1:
                w+=1
                graph[nx][ny]=0
                q.append((nx,ny))
    return w
count=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            count+=1
            graph[i][j]=0
            max_value=max(bfs(i,j),max_value)
print(count)
print(max_value)