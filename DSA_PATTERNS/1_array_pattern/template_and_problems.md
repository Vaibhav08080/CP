# ARRAY PATTERN - Foundation for DSA

## Pattern Recognition
Look for these signs:
- Finding element in array
- Checking properties of array
- Searching specific conditions
- Combining multiple arrays
- Finding subarrays/subsequences

---

## TEMPLATE: Basic Array Iteration

```python
def array_operation(arr):
    for i in range(len(arr)):
        # Process arr[i]
        pass
    return result
```

---

## TEMPLATE: Two Element Access

```python
def find_two_elements(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []
```

---

## TEMPLATE: With Frequency Counting

```python
def count_pattern(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    for num, count in freq.items():
        if count > 1:
            return num
    return -1
```

---

## PROBLEMS YOU CAN SOLVE

1. Two Sum - Find two numbers that add to target
2. Contains Duplicate - Check if any duplicate exists
3. Valid Anagram - Check if rearrangement of letters
4. Group Anagrams - Group words by anagram
5. Best Time to Buy Stock - Max profit transaction
6. Rotate Array - Rotate by k steps
7. Remove Duplicates - Keep unique elements
8. Majority Element - Element > n/2 times
9. Missing Number - Find missing in 1 to n
10. Duplicate Number - Find duplicate in 1 to n
11. First Missing Positive - Smallest missing positive
12. Product of Array Except Self - Without division

---

## EXAMPLE: Two Sum

```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Usage
print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(twoSum([3, 2, 4], 6))  # [1, 2]
```

**Time**: O(n) | **Space**: O(n)

---

## EXAMPLE: Best Time to Buy Stock

```python
def maxProfit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)
    
    return max_profit

# Usage
print(maxProfit([7, 1, 5, 3, 6, 4]))  # 5 (buy at 1, sell at 6)
print(maxProfit([7, 6, 4, 3, 1]))  # 0 (no transaction)
```

**Time**: O(n) | **Space**: O(1)

---

## EXAMPLE: Remove Duplicates

```python
def removeDuplicates(nums):
    if not nums:
        return 0
    
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    
    return j + 1

# Usage
nums = [1, 1, 2]
length = removeDuplicates(nums)
print(nums[:length])  # [1, 2]
```

**Time**: O(n) | **Space**: O(1)

---

## VARIATIONS

**Range Queries**: 
- Use prefix/suffix arrays for efficiency

**Subarray Problems**: 
- Often need sliding window or prefix sum

**Element Frequency**: 
- Use hash map to track counts

**Sorting**: 
- Sort first if order doesn't matter
