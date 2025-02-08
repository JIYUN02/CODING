mat=[]
for i in range(9):
    mat.append(list(map(int,input().split())))

max_=0
row=0
col=0
for j in range(9):
    for k in range(9):
        if mat[j][k]>max_:
            max_=mat[j][k]
            row=j
            col=k
print(max_)
print(row+1,col+1)