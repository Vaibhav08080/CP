"""
4
2
1 3 
3
2 6 4
5
5 4 6 6 1
4
3 3 3 3

"""
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print((max(arr) - min(arr)) + 1)