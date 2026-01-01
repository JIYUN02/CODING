N = list(map(int,input()))
count = [0] * 10

for i in N:
    count[i] += 1

six_nine = count[6] + count[9]
count[6] = (six_nine+1) // 2
count[9] = 0

print(max(count))
