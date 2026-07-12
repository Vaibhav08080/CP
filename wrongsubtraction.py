n,k = map(int ,input().split())
while k:
    last_digit=n%10
    if last_digit==0:
        n=n//10
    else:
        n=n-1
    k-=1
print(n)