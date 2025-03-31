a,b=map(int,input().split())
card=list(map(int,input().split()))
result=0

for j in range(a):
    for k in range(j+1,a):
        for p in range(k+1,a):
            if card[j]+card[k]+card[p]>b:
                continue
            else:
                result=max(result, card[j]+card[k]+card[p])
print(result)