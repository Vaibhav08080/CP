# DYNAMIC PROGRAMMING PATTERN

## Pattern Recognition
**Use when you see:**
- Overlapping subproblems
- Optimal substructure
- "Minimum", "Maximum", "Ways to do"
- Recursive with repetition
- Memoization possible

**Red flags**: "DP", "Optimize", "Count ways", "Min/max", "Knapsack"

---

## TEMPLATE: Top-Down (Memoization)

```python
def solve(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = solve(n-1, memo) + solve(n-2, memo)
    return memo[n]
```

---

## TEMPLATE: Bottom-Up (Tabulation)

```python
def solve(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

---

## TEMPLATE: Space Optimized

```python
def solve(n):
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr
```

---

## PROBLEMS YOU CAN SOLVE

1. Fibonacci - Classic DP
2. Climb Stairs - Ways to reach
3. House Robber - Max money
4. Coin Change - Min coins
5. Longest Increasing Subsequence - LIS
6. 0/1 Knapsack - Weight constraint
7. Longest Common Subsequence - LCS
8. Edit Distance - Min edits
9. Partition Equal Sum - Can split equally
10. Maximum Subarray - Kadane's algorithm
11. Target Sum - Assign +/- signs
12. Word Break - Can break into words

---

## EXAMPLE: Climb Stairs

```python
def climbStairs(n):
    if n <= 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Space optimized
def climbStairs_optimized(n):
    if n <= 1:
        return 1
    
    prev, curr = 1, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr

# Usage
print(climbStairs(3))  # 3 (1+1+1, 1+2, 2+1)
```

**Time**: O(n) | **Space**: O(1)

---

## EXAMPLE: Longest Increasing Subsequence

```python
def lengthOfLIS(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Usage
print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4 (2,3,7,101)
```

**Time**: O(n²) | **Space**: O(n)

---

## EXAMPLE: Coin Change

```python
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Usage
print(coinChange([1, 2, 5], 5))  # 1 (one 5-coin)
print(coinChange([2], 3))  # -1 (impossible)
```

**Time**: O(n * amount) | **Space**: O(amount)

---

## EXAMPLE: 0/1 Knapsack

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(weights, values, capacity))  # 10
```

**Time**: O(n * capacity) | **Space**: O(n * capacity)

---

## KEY POINTS

✓ Identify overlapping subproblems
✓ Define state clearly
✓ Build recurrence relation
✓ Top-down easier to code initially
✓ Bottom-up usually more efficient
✓ Space optimize when possible
✓ Consider which states you need
