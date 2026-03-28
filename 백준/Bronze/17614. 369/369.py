N = int(input())
count = 0

for i in range(1, N+1):
    count += str(i).count('3') + str(i).count('6') + str(i).count('9')
print(count)