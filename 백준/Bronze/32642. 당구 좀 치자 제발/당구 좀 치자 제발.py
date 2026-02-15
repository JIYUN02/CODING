import sys
input = sys.stdin.readline

N = int(input())
weather = input().split()

angry = 0
total = 0

for w in weather:
    if w == '1':      
        angry += 1
    else:             
        angry -= 1
    total += angry   

print(total)
