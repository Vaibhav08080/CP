n = int(input())

grid = []
count=0
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

for i in grid:
    if sum(i)>=2:
        count+=1

print(count)
