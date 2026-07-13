t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    # Distance from 0 to first gas station
    ans = arr[0]

    # Maximum distance between consecutive gas stations
    for i in range(n - 1):
        ans = max(ans, arr[i + 1] - arr[i])

    # Last gas station -> x -> last gas station
    ans = max(ans, 2 * (x - arr[-1]))

    print(ans)