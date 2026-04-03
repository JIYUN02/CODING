import math

N = int(input())
size = map(int,input().split())
T, P = map(int,input().split())

t_count = 0
for i in size:
    t_count += math.ceil(i/T)
print(t_count)
print(N//P, N%P)