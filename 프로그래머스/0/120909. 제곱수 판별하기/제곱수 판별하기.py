def solution(n):
    for i in range(1, 1001):
        if i*i==n:
            return 1
        elif i*i>n:
            return 2
    return 2