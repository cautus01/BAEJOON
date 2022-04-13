from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split()) # 행, 열 입력
graph=[] # 지도 저장
for _ in range(n): # 지도 입력받기
    graph.append(list(map(str,input())))
water=[[-1]*m for _ in range(n)] # 물이 차는 시간
animal=[[-1]*m for _ in range(n)] # 동물이 이동하는 시간
dx=[0,0,1,-1]
dy=[1,-1,0,0]
water_x=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]=='S': # 고슴도치가 있는 곳이면
            sx,sy=i,j # 고슴도치 위치 저장
        if graph[i][j]=='D': # 비버가 있는 곳이면
            Dx,Dy=i,j # 비버 위치 저장
        if graph[i][j] == '*':
            water_x.append((i, j))
def bfs_water(arr): # 물이 차는 시간 계산
    q=deque(water_x)
    for i in arr:
        water[i[0]][i[1]] = 0
    while q: # 큐가 빌 때까지
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m: # 벗어나면
                continue
            if graph[nx][ny]=='X' or graph[nx][ny]=='D': # 돌이거난 비버 굴이면
                continue
            if water[nx][ny]>=0: # 이미 방문한 곳이면
                continue
            water[nx][ny]=water[x][y]+1 # 시간 저장
            q.append((nx,ny)) # 큐에 삽입
bfs_water(water_x) # 물이 차는 시간 계산
def bfs_animal(x,y): # 동물이 이동하는 시간 계산
    q=deque()
    q.append((x,y)) # 시작점 넣기
    animal[x][y]=0 # 방문 표시
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 벗어나면
                continue
            if graph[nx][ny]=='X': # 돌이면
                continue
            if animal[nx][ny]>=0: # 이미 방문한 곳이면
                continue
            if water[nx][ny]!=-1 and water[nx][ny]<=animal[x][y]+1: # 물이 찬 곳이고 동물이 가기 전에 혹은 동시에 물이 차면
                continue
            animal[nx][ny]=animal[x][y]+1
            q.append((nx,ny))
bfs_animal(sx,sy) # 동물이 이동하는 시간 계산
if animal[Dx][Dy]!=-1: # 동물이 갈 수 있다면
    print(animal[Dx][Dy])
else: # 갈 수 없다면
    print('KAKTUS')