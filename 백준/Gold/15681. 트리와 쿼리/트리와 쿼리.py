import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

n,root,q=map(int,input().split())
parent_arr=[-1]*(n+1) # 정점의 부모
edges=[[] for _ in range(n+1)] # 간선의 정보
for _ in range(n-1):
    a,b=map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)
child=[[] for _ in range(n+1)]
tree_size=[0]*(n+1)
def makeTree(currentNode, parent):
    for node in edges[currentNode]:
        if node!=parent:
            child[currentNode].append(node)
            parent_arr[node]=currentNode
            makeTree(node, currentNode)
def countSubtreeNodes(currentNode):
    tree_size[currentNode]=1
    for node in child[currentNode]:
        countSubtreeNodes(node)
        tree_size[currentNode]+=tree_size[node]

makeTree(root, -1)
countSubtreeNodes(root)
for _ in range(q):
    u=int(input())
    print(tree_size[u])