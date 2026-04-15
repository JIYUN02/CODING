sen = input()
cam = 'CAMBRIDGE'

for i in cam:
    if i in sen:
        sen = sen.replace(i, "")
print(sen)