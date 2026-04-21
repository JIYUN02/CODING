import sys
input = sys.stdin.readline

N = int(input())
li = []

for i in range(N):
    li.append(int(input()))
new_li = sorted(li, reverse=False)

print(*new_li, sep='\n')