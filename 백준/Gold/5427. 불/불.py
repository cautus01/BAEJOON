from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs_fire(fire):
    q=deque(fire)
    for x,y in fire:
        visited1[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]=='#' or visited1[nx][ny]!=-1:
                continue
            visited1[nx][ny]=visited1[x][y]+1
            q.append((nx,ny))
def bfs_person(x,y):
    q = deque()
    q.append((x, y))
    visited2[x][y] = 0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                print(visited2[x][y]+1)
                return
            if visited2[nx][ny]!=-1 or graph[nx][ny]=='#':
                continue
            if visited1[nx][ny]!=-1 and visited1[nx][ny]<=visited2[x][y]+1:
                continue
            visited2[nx][ny]=visited2[x][y]+1
            q.append((nx,ny))
    print('IMPOSSIBLE')
t=int(input())
for _ in range(t):
    graph=[]
    m,n=map(int,input().split())
    for _ in range(n):
        graph.append(list(map(str,input())))
    visited1=[[-1]*m for _ in range(n)]
    visited2 = [[-1] * m for _ in range(n)]
    fire=[]
    p_x,p_y=0,0
    for i in range(n):
        for j in range(m):
            if graph[i][j]=='*':
                fire.append((i,j))
            if graph[i][j] == '@':
                p_x, p_y=i,j
    bfs_fire(fire)
    bfs_person(p_x, p_y)
