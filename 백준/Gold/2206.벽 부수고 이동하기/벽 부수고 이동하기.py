import sys
from collections import deque
input=sys.stdin.readline

def bfs(graph1,x,y): # bfs
    q=deque()
    q.append((x,y))
    graph1[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m: # 벗어나면
                continue
            if graph1[nx][ny]==1: # 벽이면
                continue
            if graph[nx][ny]==0 and graph1[nx][ny]!=0: # 이미 방문한 곳이면
                continue
            if graph1[nx][ny]==0: # 처음 방문한 곳이면
                graph1[nx][ny]=graph1[x][y]+1
                q.append((nx,ny))
    return graph1
n,m=map(int,input().split())
graph=[]
arr=[]
min_value=int(1e9)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))
for i in range(n):
    for j in range(m):
        if graph[i][j]==1: # 벽 부분 저장
            arr.append((i,j))
start=[[0]*m for _ in range(n)]
end=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        start[i][j]=graph[i][j]
        end[i][j] = graph[i][j]
start=bfs(start,0,0)
end=bfs(end,n-1,m-1)
if start[n-1][m-1]!=0:
    min_value=min(min_value,start[n-1][m-1])
for wall in arr:
    x,y=wall[0],wall[1]
    zero_len,end_len=int(1e9),int(1e9)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if start[nx][ny]==0 or (start[nx][ny]==1 and graph[nx][ny]==1):
            continue
        zero_len=min(zero_len,start[nx][ny])
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if end[nx][ny]==0 or (end[nx][ny]==1 and graph[nx][ny]==1):
            continue
        end_len=min(end_len,end[nx][ny])
    min_value=min(min_value,zero_len+1+end_len)
if min_value==int(1e9):
    print('-1')
else:
    print(min_value)