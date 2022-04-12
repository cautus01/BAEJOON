from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
water_x=[] # 물의 위치
for _ in range(n):
    graph.append(list(map(str,input())))
for i in range(n):
    for j in range(m):
        if graph[i][j]=='D':
            Dx,Dy=i,j # 비버의 위치
        if graph[i][j]=='S':
            sx,sy=i,j # 고슴도치의 위치
        if graph[i][j]=='*':
            water_x.append((i,j)) # 물의 위치
water=[[-1]*m for _ in range(n)] # 물의 속도
animal=[[-1]*m for _ in range(n)] # 고슴도치의 속도
def bfs_water(arr):
    q=deque(arr)
    for i in arr:
        water[i[0]][i[1]]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m: # 벗어나면
                continue
            if water[nx][ny]>=0 or graph[nx][ny]=='X' or graph[nx][ny]=='D':
                continue
            water[nx][ny]=water[x][y]+1
            q.append((nx,ny))
bfs_water(water_x)
def bfs_animal(x,y):
    q=deque()
    q.append((x,y))
    animal[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 벗어나면
                continue
            if animal[nx][ny]>=0 or graph[nx][ny]=='X':
                continue
            if water[nx][ny]!=-1 and water[nx][ny]<=animal[x][y]+1:
                continue
            animal[nx][ny]=animal[x][y]+1
            q.append((nx,ny))

bfs_animal(sx,sy)
#for i in range(n):
#    print(water[i])
#print()
#for i in range(n):
#    print(animal[i])
if animal[Dx][Dy]!=-1:
    print(animal[Dx][Dy])
else:
    print("KAKTUS")