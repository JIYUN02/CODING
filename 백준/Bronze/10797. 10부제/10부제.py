N = int(input())
car_number = list(map(int,input().split()))

count = 0
for i in car_number:
    if i == N:
        count += 1
print(count)