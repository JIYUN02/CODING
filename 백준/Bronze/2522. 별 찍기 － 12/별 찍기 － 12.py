N = int(input())
b = N - 1

for i in range(1, N+1):
    print(" " * b + "*" * i)
    b = b - 1

b = 1
for i in range(N-1, 0, -1):
    print(" " * b + "*" * i)
    b = b + 1