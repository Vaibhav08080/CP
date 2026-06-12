# BINARY SEARCH PATTERN

## Pattern Recognition
**Use when you see:**
- Sorted array/data
- "Search", "Find", "First", "Last"
- O(log n) expected
- Rotated array
- Minimize/maximize problem

**Red flags**: "Sorted", "Search", "Rotated", "Find position"

---

## TEMPLATE: Basic Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

---

## TEMPLATE: Find First Occurrence

```python
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

---

## TEMPLATE: Search on Answer

```python
def can_achieve(arr, mid, limit):
    # Check if we can achieve something with this mid value
    pass

def binary_search_answer(arr, limit):
    left, right = 0, max(arr)
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_achieve(arr, mid, limit):
            right = mid - 1
        else:
            left = mid + 1
    
    return left
```

---

## PROBLEMS YOU CAN SOLVE

1. Binary Search - Find element
2. First Bad Version - Find first bad
3. Search in Rotated Array - With rotation
4. Find First and Last Position - Of element
5. Sqrt(x) - Integer square root
6. Guess Number Higher or Lower
7. Search a 2D Matrix - In matrix
8. Koko Eating Bananas - Minimize hours
9. Capacity To Ship Packages - Minimum capacity
10. Magnetic Force Between Balls - Maximize distance
11. Minimum Days to Make m Bouquets - Days needed
12. Time Based Key-Value Store - Find value at time

---

## EXAMPLE: Find First and Last Position

```python
def searchRange(nums, target):
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    first = find_first(nums, target)
    if first == -1:
        return [-1, -1]
    
    last = find_last(nums, target)
    return [first, last]

# Usage
print(searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
```

**Time**: O(log n) | **Space**: O(1)

---

## EXAMPLE: Search in Rotated Array

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check which side is sorted
        if nums[left] <= nums[mid]:  # Left side sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right side sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Usage
print(search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
```

**Time**: O(log n) | **Space**: O(1)

---

## EXAMPLE: Koko Eating Bananas

```python
def minEatingSpeed(piles, h):
    def can_finish(speed, piles, h):
        time = 0
        for pile in piles:
            time += (pile + speed - 1) // speed  # Ceiling division
        return time <= h
    
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_finish(mid, piles, h):
            right = mid
        else:
            left = mid + 1
    
    return left

# Usage
print(minEatingSpeed([1, 1, 1, 1], 4))  # 1
print(minEatingSpeed([312884132], 968709470))  # 1
```

**Time**: O(n log(max(piles))) | **Space**: O(1)

---

## KEY POINTS

✓ Works only on sorted data
✓ Template: left <= right for inclusive search
✓ For find first: right = mid - 1 when found
✓ For find last: left = mid + 1 when found
✓ Search on answer: verify feasibility first
✓ Always O(log n) if sorted
✓ Be careful with integer overflow
