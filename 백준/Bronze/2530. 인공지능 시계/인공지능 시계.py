h, m, s = map(int,input().split())
c = int(input())

time = h*3600 + m*60 + s + c
time = time % (24 * 3600)
h = time // 3600
time = time % 3600
m = time // 60
time %= 60
s = time

print(h,m,s)



