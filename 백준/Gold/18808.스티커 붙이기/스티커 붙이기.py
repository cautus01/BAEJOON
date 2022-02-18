import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
notebook=[[0]*m for _ in range(n)]
answer=0
def check(i,j):
    for x in range(r):
        for y in range(c):
            if (notebook[x + i][y + j] == 1 and sticker[x][y] == 1):
                return False
    for x in range(r):
        for y in range(c):
            if sticker[x][y]==1:
                notebook[x + i][y + j]=1
    return True
def rotate(a):
    r_len=len(a)
    c_len=len(a[0])
    sticker_rot=[[0]*r_len for _ in range(c_len)]
    for i in range(r_len):
        for j in range(c_len):
            sticker_rot[j][r_len-i-1]=a[i][j]
    return sticker_rot
for _ in range(k):
    r,c=map(int,input().split())
    sticker=[]
    isTrue=False
    for _ in range(r):
        sticker.append(list(map(int,input().split())))
    for _ in range(4):
        for i in range(n-r+1):
            if isTrue == True:
                break
            for j in range(m-c+1):
                isTrue=check(i,j)
                if isTrue==True:
                    break
        if isTrue == True:
            break
        sticker=rotate(sticker)
        r,c=c,r
for i in range(n):
    for j in range(m):
        if notebook[i][j]==1:
            answer+=1
print(answer)