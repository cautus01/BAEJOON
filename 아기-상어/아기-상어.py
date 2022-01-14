from collections import deque

n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
baby_size=2
bx,by=0,0
eat_fish=0
time=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            bx,by=i,j
            graph[i][j]=2
def bfs(i,j):
    eat=[]
    q=deque()
    q.append((i,j))
    visited[i][j]=0
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]>baby_size or visited[nx][ny]!=-1:
                continue
            if visited[nx][ny]==-1:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
            if graph[nx][ny]<baby_size and graph[nx][ny]!=0 and visited[nx][ny]!=-1:
                eat.append((nx,ny,visited[nx][ny]))
    if not eat:
        return -1,-1,-1
    eat=sorted(eat,key=lambda x:(x[2],x[0],x[1]))
    return eat[0][0],eat[0][1],eat[0][2]
while True:
    visited=[[-1]*n for _ in range(n)]
    fx,fy,dist=bfs(bx,by)
    # print(fx,fy,dist)
    if fx==-1:
        print(time)
        break
    eat_fish+=1
    graph[bx][by]=0
    bx,by=fx,fy
    if baby_size==eat_fish:
        eat_fish=0
        baby_size+=1
    graph[bx][by]=baby_size
    time+=dist