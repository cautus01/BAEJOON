import sys
import copy
import math
input=sys.stdin.readline

n,M,k=map(int,input().split())
board=[[[] for _ in range(n)] for _ in range(n)]
for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    board[r-1][c-1].append([m,s,d])
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
def change(x,y):
    if x<0:
        x=n+x
    elif x>=n:
        x=x-n
    if y<0:
        y=y+n
    elif y>=n:
        y=y-n
    return x,y
def fireball_move():
    new_arr=[[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y]!=[]:
                for index in range(len(board[x][y])):
                    m,s,d=board[x][y][index]
                    nx=x+(s%n)*dx[d]
                    ny=y+(s%n)*dy[d]
                    nx,ny=change(nx,ny)
                    new_arr[nx][ny].append([m,s,d])
    return new_arr
def d_decide(data):
    is_check=data[0]%2
    for i in range(1,len(data)):
        if data[i]%2!=is_check:
            return False
    return True
def divide_fireball():
    new_arr = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if len(board[x][y])==1 and board[x][y]!=[]:
                new_arr[x][y].append([board[x][y][0][0],board[x][y][0][1],board[x][y][0][2]])
            if len(board[x][y])>=2:
                sum_m,sum_s,sum_d=0,0,[]
                for index in range(len(board[x][y])):
                    sum_m+=board[x][y][index][0]
                    sum_s += board[x][y][index][1]
                    sum_d.append(board[x][y][index][2])
                sum_m=math.ceil(sum_m//5)
                sum_s=math.ceil(sum_s//len(board[x][y]))
                d=d_decide(sum_d)
                sum_d = [0, 2, 4, 6] if d == True else [1, 3, 5, 7]
                for i in range(4):
                    if sum_m==0:
                        break
                    new_arr[x][y].append([sum_m,sum_s,sum_d[i]])
    return new_arr
for _ in range(k):
    new_arr=fireball_move()
    #print('---new_arr---')
    #for i in range(n):
    #    print(new_arr[i])
    board=copy.deepcopy(new_arr)
    new_arr=divide_fireball()
    board=copy.deepcopy(new_arr)
    #print('---board---')
    #for i in range(n):
    #    print(board[i])
result=0
for i in range(n):
    for j in range(n):
        if board[i][j]!=0:
            for index in range(len(board[i][j])):
                result+=board[i][j][index][0]
print(result)
