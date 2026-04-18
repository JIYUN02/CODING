def solution(a, b):
    total = 0
    
    start = min(a, b)
    end = max(a, b)
    
    for i in range(start, end + 1):
        total += i
        
    return total

solution(3,5)
        