n = int(input())

li = []
for i in range(n):
    k = int(input())
    li.append(k)
obj = li[0]
ma = max(li)
mi = min(li)

if obj >= ma:
    print('hard')
elif obj <= mi:
    print('ez')
else:
    print('?')