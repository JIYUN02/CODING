a=input()
dic={"c=":1, "c-":1, "dz=":1, "d-":1, "lj":1, "nj":1, "s=":1, "z=":1}

for i in dic:
    a=a.replace(i,"*")
    
print(len(a))