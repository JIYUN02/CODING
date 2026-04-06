N = int(input())
menu = []

for i in range(N):
    menu.append(int(input()))

total = 0
M = int(input())
for j in range(M):
    number = int(input())
    total += menu[number-1]

print(total)