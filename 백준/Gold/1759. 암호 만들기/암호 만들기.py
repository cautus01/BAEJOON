from itertools import combinations
import sys
input=sys.stdin.readline

l,c=map(int,input().split())
s=list(map(str,input().split()))
vowel=[i for i in s if i in ['a', 'e', 'i', 'o', 'u']]
conso=[i for i in s if i not in ['a', 'e', 'i', 'o', 'u']]
password=set()
for i in vowel:
    for con in list(combinations(conso,2)): # con = ('t', 'c')
        result=[i]+list(con)
        remain=[i for i in s if i not in result]
        for r in list(combinations(remain,l-3)):
            answer=result + list(r)
            password.add(''.join(sorted(answer)))
password=sorted(password)
for i in password:
    print(i)