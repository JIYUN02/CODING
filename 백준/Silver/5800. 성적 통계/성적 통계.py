N = int(input())

for i in range(N):
    re = list(map(int,input().split()))
    re.pop(0)
    re = sorted(re, reverse=True)

    count = []
    for j in range(len(re)-1):
        if j == len(re):
            break
        else:
            gap = abs(re[j]-re[j+1])
            count.append(gap)

    print(f'Class {i+1}')
    print(f'Max {re[0]}, Min {re[-1]}, Largest gap {max(count)}')