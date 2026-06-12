# PREFIX SUM PATTERN

## Pattern Recognition
**Use when you see:**
- Range sum queries
- Subarray sum problems
- "Sum from index i to j"
- Need repeated sum calculations
- Efficiency is important

**Red flags**: "Range query", "Subarray sum", "Sum between"

---

## TEMPLATE: Basic Prefix Sum

```python
def prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    
    return prefix

# Query sum from index i to j (inclusive)
def range_sum(prefix, i, j):
    return prefix[j + 1] - prefix[i]
```

---

## TEMPLATE: 2D Prefix Sum

```python
def prefix_sum_2d(matrix):
    m, n = len(matrix), len(matrix[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = (
                matrix[i-1][j-1] +
                prefix[i-1][j] +
                prefix[i][j-1] -
                prefix[i-1][j-1]
            )
    
    return prefix

# Query sum in rectangle from (r1,c1) to (r2,c2)
def range_sum_2d(prefix, r1, c1, r2, c2):
    return (
        prefix[r2+1][c2+1] -
        prefix[r1][c2+1] -
        prefix[r2+1][c1] +
        prefix[r1][c1]
    )
```

---

## TEMPLATE: Find Subarray with Sum

```python
def find_subarray_sum(arr, target):
    prefix_sum = 0
    sum_map = {0: -1}  # sum -> index
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        if prefix_sum - target in sum_map:
            return [sum_map[prefix_sum - target] + 1, i]
        
        if prefix_sum not in sum_map:
            sum_map[prefix_sum] = i
    
    return [-1, -1]
```

---

## PROBLEMS YOU CAN SOLVE

1. Prefix Sum - Calculate efficiently
2. Range Sum Query - Query repeated sums
3. Subarray Sum Equals K - Find subarray
4. Continuous Subarray Sum - Divisible by k
5. Maximum Subarray - Kadane with prefix
6. Subarrays with Sum K - Count subarrays
7. Range Sum Query 2D - 2D matrix
8. Product of Array Except Self - Without division
9. Paint House - Minimum cost painting
10. Majority Element - Find majority
11. Left and Right Sum Differences
12. Plates Between Candles - Count plates

---

## EXAMPLE: Range Sum Query

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    
    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]

# Usage
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))  # 1 (-2 + 0 + 3)
print(obj.sumRange(2, 5))  # -1 (3 + -5 + 2 + -1)
```

**Time**: O(1) per query | **Space**: O(n)

---

## EXAMPLE: Subarray Sum Equals K

```python
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    sum_map = {0: 1}  # sum -> frequency
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - k in sum_map:
            count += sum_map[prefix_sum - k]
        
        sum_map[prefix_sum] = sum_map.get(prefix_sum, 0) + 1
    
    return count

# Usage
print(subarraySum([1, 1, 1], 2))  # 2 ([1,1] at indices 0-1 and 1-2)
print(subarraySum([1, 2, 3], 3))  # 2 ([3] and [1,2])
```

**Time**: O(n) | **Space**: O(n)

---

## EXAMPLE: Product of Array Except Self

```python
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    # Left products
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]
    
    # Right products
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    
    return result

# Usage
print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
```

**Time**: O(n) | **Space**: O(1) (not counting output)

---

## EXAMPLE: Range Sum Query 2D

```python
class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (
                    matrix[i-1][j-1] +
                    self.prefix[i-1][j] +
                    self.prefix[i][j-1] -
                    self.prefix[i-1][j-1]
                )
    
    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.prefix[row2+1][col2+1] -
            self.prefix[row1][col2+1] -
            self.prefix[row2+1][col1] +
            self.prefix[row1][col1]
        )

# Usage
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))  # 11
```

**Time**: O(1) per query | **Space**: O(m*n)

---

## KEY POINTS

✓ Precompute to optimize repeated queries
✓ 1D: prefix[i] = prefix[i-1] + arr[i]
✓ 2D: Include overlaps, exclude under-counting
✓ Query: right - left (adjust indices)
✓ Perfect for "sum of subarray" problems
✓ Combine with hash map for "sum equals k"
