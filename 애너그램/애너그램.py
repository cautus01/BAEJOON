import sys
n=int(sys.stdin.readline())
def func(s):
    if len(s)==len(string):
        sys.stdout.write(s)
        sys.stdout.write('\n')
        return
    last = None
    for i in range(len(string)):
        if visited[i]==0 and string[i]!=last:
            visited[i]=1
            last=string[i]
            func(s+string[i])
            visited[i]=0
for i in range(n):
    string=list(sys.stdin.readline().rstrip())
    string.sort()
    visited=[0]*len(string)
    func('')