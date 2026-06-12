meow = []

for i in range(2):
    meow.append(input().lower())

if meow[0] < meow[1]:
    print(-1)
elif meow[0] > meow[1]:
    print(1)
else:
    print(0)        