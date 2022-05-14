import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
cctv=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if 1<=graph[i][j]<=5:
            cctv.append((i,j))
min_value=int(1e9)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def upd(x,y,d):
    d%=4
    while True:
        x=x+dx[d]
        y=y+dy[d]
        if x<0 or y<0 or x>=n or y>=m:
            return
        if graph1[x][y]==6:
            return
        if 1<=graph1[x][y]<=5:
            continue
        graph1[x][y]=7
for k in range(4**len(cctv)):
    graph1=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            graph1[i][j]=graph[i][j]
    tmp=k
    for i in range(len(cctv)):
        d=tmp%4
        tmp//=4
        x=cctv[i][0]
        y=cctv[i][1]
        if graph1[x][y]==1:
            upd(x,y,d)
        if graph1[x][y] == 2:
            upd(x, y, d)
            upd(x, y, d+2)
        if graph1[x][y] == 3:
            upd(x, y, d)
            upd(x, y, d+1)
        if graph1[x][y] == 4:
            upd(x, y, d)
            upd(x, y, d+1)
            upd(x, y, d+3)
        if graph1[x][y] == 5:
            upd(x, y, d)
            upd(x, y, d+1)
            upd(x, y, d+2)
            upd(x, y, d+3)
    result=0
    for i in range(n):
        for j in range(m):
            if graph1[i][j]==0:
                result+=1
    min_value=min(min_value,result)
print(min_value)