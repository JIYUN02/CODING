def solution(s):
    string_len = len(s)
    if string_len % 2 != 0:
        result = s[int(string_len/2)]
    else:
        result = s[int(string_len/2)-1:int(string_len/2)+1]
    return result