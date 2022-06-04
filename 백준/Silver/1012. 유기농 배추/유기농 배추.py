from collections import deque
import sys
input=sys.stdin.readline

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
            if graph[nx][ny]==1:
                q.append((nx,ny))
                visited[nx][ny]=0
t=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]
    for _ in range(k):
        y,x=map(int,input().split())
        graph[x][y]=1
    count=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and visited[i][j]==-1:
                bfs(i,j)
                count+=1
    print(count)