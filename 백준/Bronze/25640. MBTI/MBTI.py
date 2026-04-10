jh_mbti = input()
N = int(input())
li = []

for i in range(N):
    li.append(input())

count = 0
for j in li:
    if j == jh_mbti:
        count+=1
print(count)    