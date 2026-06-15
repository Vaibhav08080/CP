t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print("YES" if n - k >= k else "NO")