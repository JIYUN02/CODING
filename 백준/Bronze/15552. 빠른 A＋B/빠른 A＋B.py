import sys
a=int(input())

for n in range(a):
    b,c=map(int,sys.stdin.readline().split())
    print(b+c)