from collections import deque

m,n,h=map(int,input().split())
graph=[]
for _ in range(h):
    data=[]
    for j in range(n):
        data.append(list(map(int,input().split())))
    graph.append(data)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
q=deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j]==1:
                q.append((k,i,j))
while q:
    height,x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if graph[height][nx][ny]==-1 or graph[height][nx][ny]>=1:
            continue
        if graph[height][nx][ny]==0:
            graph[height][nx][ny]=graph[height][x][y]+1
            q.append((height,nx,ny))
    for i in (-1,1):
        nh=height+i
        if nh<0 or nh>=h:
            continue
        if graph[nh][x][y]==-1 or graph[nh][x][y]>=1:
            continue
        if graph[nh][x][y]==0:
            graph[nh][x][y]=graph[height][x][y]+1
            q.append((nh,x,y))
# print(graph)
max_value=0
def func(h,n,m):
    global max_value
    for k in range(h):
        for i in range(n):
            max_value = max(max_value, max(graph[k][i]))
            for j in range(m):
                if graph[k][i][j]==0:
                    return -1
    return max_value-1
print(func(h,n,m))