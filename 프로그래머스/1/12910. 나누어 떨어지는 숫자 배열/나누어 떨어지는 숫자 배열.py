def solution(arr, divisor):
    new_li = []
    for i in arr:
        if i % divisor == 0:
            new_li.append(i)
    if len(new_li) == 0:
        return [-1]
    else:
        return sorted(new_li, reverse = False)        