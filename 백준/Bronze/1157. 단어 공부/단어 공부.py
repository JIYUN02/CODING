a=input().upper()
dic={}

for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

value_max=max(dic.values())
value=[]

for key,vv in dic.items():
    if value_max==vv:
        value.append(key)

if len(value)>1:
    print("?")
else:
    print(value[0])