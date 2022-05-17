import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
year=1
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def melt(x,y):
    count=0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx>=n or ny>=m:
            continue
        if graph[nx][ny]==0:
            count+=1
    if graph[x][y]-count<=0:
        new_arr[x][y]=0
    else:
        new_arr[x][y]-=count
def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if visited[nx][ny]!=-1:
                continue
            if new_arr[nx][ny]!=0:
                q.append((nx,ny))
                visited[nx][ny]=0
while True:
    new_arr=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_arr[i][j]=graph[i][j] # graph 복사
    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0:
                melt(x,y) # 빙산 녹이기
    ice_count=0 # 빙산 덩어리 개수
    visited = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if new_arr[i][j]!=0 and visited[i][j]==-1:
                bfs(i,j)
                ice_count+=1
    if ice_count>=2:
        print(year)
        break
    sum_value=0
    for i in range(n):
        sum_value+=sum(new_arr[i])
    if sum_value==0:
        print(0)
        break
    # graph에 new_arr 저장
    for i in range(n):
        for j in range(m):
            graph[i][j]=new_arr[i][j]
    year+=1