round = int(input())
a_score, b_score = 0, 0

for i in range(round):
    a_round_score, b_round_score = map(int,input().split())
    if a_round_score > b_round_score:
        a_score += 1
    elif a_round_score < b_round_score:
        b_score += 1
    else:
        pass
print(a_score, b_score, end=" ")