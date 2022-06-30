from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[]
for _ in range(n):
    graph.append(input().rstrip())
visit=[[0]*n for _ in range(n)]
visit_rg=[[0]*n for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
count=0
rg_count=0

def bfs(x,y,color):
    q=deque()
    q.append((x,y))
    visit[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n: # 벗어난다면
                continue
            if graph[nx][ny]!=color: # 색깔이 다르다면
                continue
            if graph[nx][ny]==color and not visit[nx][ny]:# 색깔이 같고 방문하지 않는 곳이라면
                q.append((nx,ny))
                visit[nx][ny]=1
def rg_bfs(x,y,color):
    q=deque()
    q.append((x,y))
    visit_rg[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n: # 벗어난다면
                continue
            if graph[nx][ny] not in color: # 색깔이 다르다면
                continue
            if graph[nx][ny] in color and not visit_rg[nx][ny]:# 색깔이 같고 방문하지 않는 곳이라면
                q.append((nx,ny))
                visit_rg[nx][ny]=1
for i in range(n):
    for j in range(n):
        if not visit[i][j]: # 방문하지 않았다면
            bfs(i,j,graph[i][j])
            count+=1
for i in range(n):
    for j in range(n):
        if not visit_rg[i][j]: # 방문하지 않았다면
            if graph[i][j] in ['R','G']:
                rg_bfs(i,j,['R','G'])
            else:
                rg_bfs(i, j, ['B'])
            rg_count+=1
print(count,rg_count)