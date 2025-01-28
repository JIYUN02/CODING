a=int(input())
count1=a


for i in range(a):
    b=list(input())
    for j in range (0,len(b)-1):
        if b[j]==b[j+1]:
            pass
        elif b[j] in b[j+1:]:
            count1-=1
            break
print(count1)