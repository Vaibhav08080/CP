string=input()
ar=[]
result=""
for i in string:
    if i.isnumeric():
        ar.append(i)
sorted_arr=sorted(ar)    
for i in sorted_arr:
    result+=i
    result+="+"
    
# result-="+"
n=len(result)
print(result[0:n-1])
    
            