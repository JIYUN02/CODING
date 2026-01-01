min_score = list(map(int,input().split()))
man_score = list(map(int,input().split()))

if sum(min_score) > sum(man_score):
    print(sum(min_score))
elif sum(min_score) == sum(man_score):
    print(sum(min_score))
else:
    print(sum(man_score))