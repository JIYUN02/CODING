def solution(phone_number):
    result = phone_number[-4:]
    phone_number_len = len(phone_number)
    answer = (phone_number_len-4) * "*" + result
    return answer
    