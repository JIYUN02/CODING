M = int(input())
N = int(input())

total = 0
minimum = 0

for i in range(1, 101):
    square = i * i
    
    if square > N:
        break

    if square >= M:
        total += square
        if minimum == 0:
            minimum = square

if total > 0:
    print(total)
    print(minimum)
else:
    print(-1)