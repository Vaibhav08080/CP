"""
8 5
10 9 8 7 7 7 5 5
"""
n, k = map(int, input().split())
num=list(map(int , input().split()))
count=0
for i in num:
    if i>=num[k-1] and i>0:
        count+=1
print(count)
