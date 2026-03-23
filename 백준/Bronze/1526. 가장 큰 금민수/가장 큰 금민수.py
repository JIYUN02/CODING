N = int(input())

for i in range(N, 0, -1):
    for j in str(i):
        if j != '4' and j != '7':
            break
    else:
        print(i)
        break