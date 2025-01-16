a=int(input())

for i in range(a):
    b,c=input().split()
    b=int(b)
    for j in c:
        print(j*b,end='')
    print()