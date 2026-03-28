import math

N, W, H = map(int,input().split())
for i in range(N):
    leng = int(input())
    if leng <= math.sqrt((W**2) + (H**2)):
        print("DA")
    else:
        print("NE")