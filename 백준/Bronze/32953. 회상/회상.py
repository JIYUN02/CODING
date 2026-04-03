N, M = map(int,input().split())
student = {}

for i in range(N):
    k = int(input())
    student_number = map(int,input().split())
    for j in student_number:
        student[j] = student.get(j, 0) + 1

count = 0
for q in student.values():
    if q >= M:
        count += 1
print(count)
