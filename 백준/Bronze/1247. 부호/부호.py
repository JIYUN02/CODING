for i in range(3):
    N = int(input())
    sum = 0
    for i in range(N):
        value = int(input())
        sum += value
    if sum == 0:
        print(0)
    elif sum > 0:
        print('+')
    else:
        print('-')