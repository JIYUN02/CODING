for i in range(3):
    li = []
    a,b,c,d = map(int,input().split())
    li.append(a)
    li.append(b)
    li.append(c)
    li.append(d)
    if li.count(0) == 1:
        print("A")
    elif li.count(0) == 2:
        print("B")
    elif li.count(0) == 3:
        print("C")
    elif li.count(0) == 4:
        print("D")
    elif li.count(1) == 4:
        print("E")