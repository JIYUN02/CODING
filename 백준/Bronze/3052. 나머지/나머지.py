a=set()
count=0

for i in range(10):
    n=int(input())
    fin=n%42
    a.add(fin)
print(len(a))