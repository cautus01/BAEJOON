from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
board=[]
max_value=0
for _ in range(n):
    board.append(list(map(int,input().split())))
def up():
    board_up=[[0]*n for _ in range(n)]
    for i in range(n):
        q=deque()
        for j in range(n):
            q.append(board_k[j][i])
        stack=[]
        s=0
        while q:
            x=q.popleft()
            if x==0:
                continue
            if stack==[]:
                stack.append(x)
                continue
            if stack[-1]==x and s==1:
                stack.append(x)
                s=0
                continue
            if stack[-1]==x and s==0:
                stack[-1]=x*2
                s=1
                continue
            if stack[-1] != x:
                stack.append(x)
                s=0
        for l in range(len(stack)):
            board_up[l][i]=stack[l]
    return board_up
def down():
    board_up=[[0]*n for _ in range(n)]
    for i in range(n):
        q=deque()
        for j in range(n):
            q.append(board_k[n-j-1][i])
        stack=[]
        s=0
        while q:
            x=q.popleft()
            if x==0:
                continue
            if stack==[]:
                stack.append(x)
                continue
            if stack[-1]==x and s==1:
                stack.append(x)
                s=0
                continue
            if stack[-1]==x and s==0:
                stack[-1]=x*2
                s=1
                continue
            if stack[-1] != x:
                stack.append(x)
                s=0
        for l in range(len(stack)):
            board_up[n-l-1][i]=stack[l]
    return board_up
def left():
    board_up=[[0]*n for _ in range(n)]
    for i in range(n):
        q=deque()
        for j in range(n):
            q.append(board_k[i][j])
        stack=[]
        s=0
        while q:
            x=q.popleft()
            if x==0:
                continue
            if stack==[]:
                stack.append(x)
                continue
            if stack[-1]==x and s==1:
                stack.append(x)
                s=0
                continue
            if stack[-1]==x and s==0:
                stack[-1]=x*2
                s=1
                continue
            if stack[-1] != x:
                stack.append(x)
                s=0
        for l in range(len(stack)):
            board_up[i][l]=stack[l]
    return board_up
def right():
    board_up=[[0]*n for _ in range(n)]
    for i in range(n):
        q=deque()
        for j in range(n):
            q.append(board_k[i][n-j-1])
        stack=[]
        s=0
        while q:
            x=q.popleft()
            if x==0:
                continue
            if stack==[]:
                stack.append(x)
                continue
            if stack[-1]==x and s==1:
                stack.append(x)
                s=0
                continue
            if stack[-1]==x and s==0:
                stack[-1]=x*2
                s=1
                continue
            if stack[-1] != x:
                stack.append(x)
                s=0
        for l in range(len(stack)):
            board_up[i][n-l-1]=stack[l]
    return board_up
for k in range(5**5): # 5**5
    board_k=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            board_k[i][j]=board[i][j]
    for i in range(5):
        d=k%5
        k//=5
        if d==0:
            continue
        if d==1:
            board_k=right()
        if d==2:
            board_k=up()
        if d==3:
            board_k=down()
        if d==4:
            board_k=left()
    result=0
    for i in range(n):
        for j in range(n):
            result=max(result,board_k[i][j])
    max_value=max(max_value,result)
print(max_value)