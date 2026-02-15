N = int(input())
depart = input()
s, b, a = 0, 0, 0

for i in depart:
    if i == 'S':
        s += 1
    elif i == 'B':
        b += 1
    else:
        a += 1

m = max(s, b, a)

if s == b == a:
    print("SCU")
elif s == m and b == m:
    print("BS")
elif s == m and a == m:
    print("SA")
elif b == m and a == m:
    print("BA")
elif s == m:
    print("S")
elif b == m:
    print("B")
else:
    print("A")