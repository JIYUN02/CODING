N,B=map(int,input().split())
result=[]

while N>0:
    na=N%B
    if na<10:
        result.append(str(na))
    else:
        result.append(chr(na-10+ord('A')))
    N//=B
    
result.reverse()
print(''.join(result))