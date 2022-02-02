from collections import deque

n=int(input())
graph=[[0]*n for _ in range(n)]
dir_data={}
k=int(input())
time=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for _ in range(k):
    a,b=map(int,input().split())
    graph[a-1][b-1]=2
l=int(input())
for _ in range(l):
    x,c=map(str,input().split())
    dir_data[int(x)]=c
d,x,y=0,0,0
graph[x][y]=1
q=deque()
q.append((x,y))
def direction(d,c):
    result=0
    if c=='L':
        result=d-1
    else:
        result=d+1
    if result==-1:
        result=3
    if result==4:
        result=0
    return result
while True:
    time+=1
    x=x+dx[d]
    y=y+dy[d]
    if x<0 or y<0 or x>=n or y>=n:
        break
    if graph[x][y]==1:
        break
    q.append((x,y))
    if graph[x][y]!=2:
        graph[x][y]=1
        t_x,t_y=q.popleft()
        graph[t_x][t_y]=0
    if graph[x][y]==2:
        graph[x][y]=1
    if time in dir_data:
        d=direction(d,dir_data[time])

print(time)