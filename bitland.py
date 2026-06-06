n=int(input())
summ=0
for i in range(n):
    operation = input()
    if "+" in operation:
        summ+=1
    else:
        summ-=1
print(summ)

