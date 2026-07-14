def solution(a, b):
    new_ab = str(a)+str(b)
    new_ba = str(b)+str(a)
    if new_ab > new_ba:
        return int(new_ab)
    else:
        return int(new_ba)