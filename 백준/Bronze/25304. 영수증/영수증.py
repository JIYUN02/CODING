a=int(input())
b=int(input())
e=0

for i in range(b):
    c,d=map(int,input().split())
    e=e+c*d
if a==e:
    print("Yes")
else:
    print("No")