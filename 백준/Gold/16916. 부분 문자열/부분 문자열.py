import sys
input=sys.stdin.readline

string=input()
s=input()


if s[:-1] in string[:-1]:
    print(1)
else:
    print(0)
