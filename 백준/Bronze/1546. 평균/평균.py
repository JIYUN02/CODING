a=int(input())
pp=list(map(int,input().split()))
score=0
    
ms=max(pp)

for j in range(a):
    score+=pp[j]/ms*100
print(score/a)
    
    