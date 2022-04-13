from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(str,input())))
water=[[-1]*m for _ in range(n)]
animal=[[-1]*m for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for i in range(n):
    for j in range(m):
        if graph[i][j]=='S':
            sx,sy=i,j
        if graph[i][j]=='D':
            Dx,Dy=i,j
def bfs_water():
    q=deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '*':
                q.append((i, j)) # 큐에 시작점 넣기
                water[i][j]=0 # 방문처리
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]=='X' or graph[nx][ny]=='D':
                continue
            if water[nx][ny]>=0:
                continue
            water[nx][ny]=water[x][y]+1
            q.append((nx,ny))
bfs_water()
def bfs_animal(x,y):
    q=deque()
    q.append((x,y))
    animal[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny]=='X':
                continue
            if animal[nx][ny]>=0:
                continue
            if water[nx][ny]!=-1 and water[nx][ny]<=animal[x][y]+1:
                continue
            animal[nx][ny]=animal[x][y]+1
            q.append((nx,ny))
bfs_animal(sx,sy)
if animal[Dx][Dy]==-1:
    print('KAKTUS')
else:
    print(animal[Dx][Dy])