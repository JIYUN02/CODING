bk=0
ck=0
result=[]
dic={"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}

for i in range(20):
    a,b,c=map(str,input().split())
    if c=="P":
        pass
    elif c!="P":
        bk+=float(b)
    for j in dic:
        if j==c:
            ck=dic[c]
            result.append(float(b)*ck)
        else:
            pass
            
f=sum(result)
    
print(f/bk)