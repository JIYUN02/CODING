total = 0
li = []

for i in range(4):
    a, b = map(int,input().split())
    total = total - a + b
    li.append(total)

print(max(li))