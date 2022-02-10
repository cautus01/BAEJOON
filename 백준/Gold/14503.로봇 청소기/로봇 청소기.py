n,m=map(int,input().split())
x,y,d=map(int,input().split())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
count=1
graph[x][y]=2
turn_time=0
def direction_change(x):
    x=x-1
    if x==-1:
        return 3
    return x
while True:
    d=direction_change(d)
    nx=x+dx[d]
    ny=y+dy[d]
    if graph[nx][ny]==0:
        graph[nx][ny]=2
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    if turn_time==4:
        nx=x-dx[d]
        ny=y-dy[d]
        if graph[nx][ny]==2:
            x=nx
            y=ny
        else:
            break
        turn_time=0
print(count)