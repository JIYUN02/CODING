def solution(arr):
    if len(arr) == 1:
        return -1
    else:
        arr_min = min(arr)
        arr.remove(arr_min)
        return arr