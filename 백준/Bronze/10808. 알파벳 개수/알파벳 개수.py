from collections import Counter

string=input()
counter=Counter(string)
data=[]
for i in range(97,123):
    data.append(chr(i))
for i in data:
    if i not in counter:
        print(0,end=' ')
    else:
        print(counter[i],end=' ')