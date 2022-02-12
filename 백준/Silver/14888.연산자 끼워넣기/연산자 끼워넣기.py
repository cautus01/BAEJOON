n=int(input())
arr=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
min_value=int(1e9)
max_value=-int(1e9)

def dfs(result,index):
    global min_value,max_value
    global add,sub,mul,div
    if index==n:
        min_value=min(min_value,result)
        max_value=max(max_value,result)
    else:
        if add>0:
            add-=1
            dfs(result+arr[index],index+1)
            add+=1
        if sub>0:
            sub -= 1
            dfs(result - arr[index], index + 1)
            sub += 1
        if mul>0:
            mul -= 1
            dfs(result * arr[index], index + 1)
            mul += 1
        if div>0:
            div -= 1
            if result<0:
                dfs(-(abs(result)//arr[index]), index + 1)
            else:
                dfs(result // arr[index], index + 1)
            div += 1
dfs(arr[0],1)
print(max_value)
print(min_value)
