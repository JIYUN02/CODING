a,b=input().split()
li={"A":10, "B":11, "C":12, "D":13, "E":14, "F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35}

result=0
a=list(a)
lo=len(a)

for i in range(lo):
    if a[i].isalpha():
        result+=li.get(a[i])*(int(b)**(lo-i-1))
    else:
        result+=int(a[i])*(int(b)**(lo-i-1))

print(result)

    