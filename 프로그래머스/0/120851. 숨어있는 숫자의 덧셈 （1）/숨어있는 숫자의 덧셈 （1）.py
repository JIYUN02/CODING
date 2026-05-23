def solution(my_string):
    li = ['0','1','2','3','4','5','6','7','8','9']
    result = 0

    for i in my_string:
        if i in li:
            result += int(i)

    return result