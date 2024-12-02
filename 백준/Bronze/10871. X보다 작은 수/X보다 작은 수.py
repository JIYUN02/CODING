a,b=map(int,input().split())
_list=list(map(int,input().split()))

for c in range(a):
    if _list[c]<b:
        print(_list[c],end=" ")