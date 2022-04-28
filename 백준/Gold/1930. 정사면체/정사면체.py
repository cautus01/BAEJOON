import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    data=list(map(int,input().split()))
    arr1=data[:4] # 정사면체 1
    arr2=data[4:] # 정사면체 2
    arr1_dic={'down':arr1[0],'side':arr1[1:]} # 기준점 밑면과 옆면
    is_True = False

    arr2_possible=[]
    arr2_possible.append([arr2[0],arr2[1:]])
    arr2_possible.append([arr2[1], [arr2[2],arr2[0],arr2[3]]])
    arr2_possible.append([arr2[2],[arr2[1],arr2[3],arr2[0]]])
    arr2_possible.append([arr2[3], [arr2[1], arr2[0], arr2[2]]])
    is_True = False
    for i in range(4):
        if arr2_possible[i][0]!=arr1[0]:
            continue
        side=arr2_possible[i][1]
        copy=[side[0],side[1],side[2]]
        side_possible=[]
        side_possible.append(side)
        for _ in range(2):
            front=copy.pop(0)
            copy.append(front)
            arr=[copy[0],copy[1],copy[2]]
            side_possible.append(arr)
        if arr1_dic['side'] in side_possible:
            print(1)
            is_True=True
            break
    if is_True==False:
        print(0)
