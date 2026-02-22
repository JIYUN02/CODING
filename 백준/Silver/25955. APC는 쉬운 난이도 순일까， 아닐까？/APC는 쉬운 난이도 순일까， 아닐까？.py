N = int(input())
li = input().split()
dic = {'B' : 1, 'S' : 2, 'G' : 3, 'P' : 4, 'D' : 5}

sorted_li = sorted(li, key = lambda x: (dic[x[0]], -int(x[1:])))

diff = []
for i in range(N):
    if li[i] != sorted_li[i]:
        diff.append(i)

if len(diff) == 0:
    print('OK')
else:
    print('KO')
    a = sorted_li[diff[0]]
    b = sorted_li[diff[1]]

    if (dic[a[0]], -int(a[1:])) <= (dic[b[0]], -int(b[1:])):
        print(a,b)
    else:
        print(b,a)