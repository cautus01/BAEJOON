from collections import deque

n,l,r=map(int,input().split())
graph=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(n):
    graph.append(list(map(int,input().split())))
days=0
def bfs(fx,fy):
    q=deque()
    data = [] # 좌표 저장
    p_num = 0
    q.append((fx,fy))
    data.append((fx,fy))
    p_num+=graph[fx][fy]
    visited[fx][fy]=union
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if visited[nx][ny]!=0:
                continue
            if l<=abs(graph[nx][ny]-graph[x][y])<=r and visited[nx][ny]==0:
                visited[nx][ny]=union
                q.append((nx,ny))
                data.append((nx,ny))
                p_num+=graph[nx][ny]
    p_num=p_num//len(data)
    for i in data:
        x,y=i
        graph[x][y]=p_num
    return
while True:
    union=0 # 연합
    index=0 # 횟수
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                union+=1
                index+=1
                bfs(i,j)
    if index==n*n:
        break
    else:
        days += 1
print(days)
