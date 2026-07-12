b, c = map(int, input().split())

year = 0
while b <=c:
    year += 1
    b *= 3
    c *= 2

print(year)