M = int(input())
N = int(input())
result = []
sum = 0
min = 0

for i in range(1, 101):
    result.append(i*i)

for j in result:
    if M <= j <= N:
        sum += j

for k in result:
    if M <= k <= N:
        min += k
        break

if sum and min > 0:
    print(sum)
    print(min)
else:
    print(-1)