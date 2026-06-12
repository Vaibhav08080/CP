stringinput=input()
arrayf=[]
for i in range(len(stringinput)):
    if stringinput[i] in arrayf:
        continue
    else:
        arrayf.append(stringinput[i])
if len(arrayf)%2!=0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")