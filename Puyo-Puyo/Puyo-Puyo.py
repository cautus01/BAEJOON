from collections import deque

graph=[]
for _ in range(12):
    graph.append(list(map(str,input())))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
count=0
def bfs(i,j,char):
    q=deque()
    q.append((i,j))
    visited[i][j]=0
    chain.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=12 or ny>=6:
                continue
            if graph[nx][ny]=='.' or visited[nx][ny]!=-1:
                continue
            if graph[nx][ny]==char:
                q.append((nx,ny))
                visited[nx][ny]=0
                chain.append([nx,ny])
def down():
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11,j,-1):
                if graph[k][i]=='.' and graph[j][i]!='.':
                    graph[k][i]=graph[j][i]
                    graph[j][i]='.'
                    break
while True:
    visited=[[-1]*6 for _ in range(12)]
    isTrue=False
    for i in range(12):
        for j in range(6):
            if graph[i][j]!='.' and visited[i][j]==-1:
                chain=[]
                bfs(i,j,graph[i][j])
                if len(chain)>=4:
                    isTrue=True
                    for c in chain:
                        x,y=c
                        graph[x][y]='.'
    if isTrue==False:
        break
    count+=1
    down()
print(count)