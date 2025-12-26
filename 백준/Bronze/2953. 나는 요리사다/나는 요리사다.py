result = []
for i in range(5):
    score = list(map(int,input().split()))
    result.append(sum(score))
max_value = max(result)
print(result.index(max_value)+1,max_value, end=" ")