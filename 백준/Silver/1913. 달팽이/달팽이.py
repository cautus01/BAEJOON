import sys

input=sys.stdin.readline
n=int(input())
m=int(input())
mx,my,x,y=0,0,0,0
graph=[[0]*n for _ in range(n)]
num=n*n
dx=[1,0,-1,0]
dy=[0,1,0,-1]
d=0
graph[x][y]=num
num-=1
while num>0:
    if (x,y)==(n-1,0):
        d=1
    if (x, y) == (n-1, n-1):
        d = 2
    if (x, y) == (0, n - 1):
        d = 3
    if graph[x + dx[d]][y + dy[d]]!=0:
        d=0 if d==3 else d+1
    nx = x + dx[d]
    ny = y + dy[d]
    graph[nx][ny]=num
    if num==m:
        mx,my=nx,ny
    num-=1
    x,y=nx,ny
for i in range(n):
    for j in range(n):
        print(graph[i][j],end=' ')
    print()
print(mx+1,my+1)