a=input().upper()
dic={}

for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

value_max=max(dic.values())
list=[]

for key, value in dic.items():
    if value==value_max:
        list.append(key)

if len(list)>1:
    print("?")
else:
    print(list[0])
        
    