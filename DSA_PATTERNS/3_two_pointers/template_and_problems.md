# TWO POINTERS PATTERN

## Pattern Recognition
**Use when you see:**
- Sorted array
- Container, pairs, triplets
- "Two numbers", "Reverse"
- Remove duplicates from sorted
- Partition array

**Red flags**: "Pairs", "Triplet", "Reverse", "Sorted"

---

## TEMPLATE: Basic Two Pointers

```python
def two_pointers(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

---

## TEMPLATE: Remove Duplicates (Inplace)

```python
def remove_duplicates(arr):
    left = 0
    
    for right in range(1, len(arr)):
        if arr[right] != arr[left]:
            left += 1
            arr[left] = arr[right]
    
    return left + 1
```

---

## TEMPLATE: Partition Array

```python
def partition(arr, pivot):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] >= pivot:
            right -= 1
        
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    return left
```

---

## PROBLEMS YOU CAN SOLVE

1. Two Sum II - Sorted array
2. 3Sum - Find all triplets
3. 3Sum Closest - Closest to target
4. Container With Most Water - Max area
5. Sort Colors - 0,1,2 sorting
6. Reverse String - Reverse array
7. Move Zeros - Move zeros to end
8. Palindrome Validation - Check if palindrome
9. Remove Nth Node From End
10. Valid Triangle Number - Valid triangles count
11. Squares of Sorted Array - Square each element
12. Next Permutation - Next lexicographic order

---

## EXAMPLE: Two Sum II

```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# Usage
print(twoSum([2, 7, 11, 15], 9))  # [1, 2]
print(twoSum([2, 3, 4], 6))  # [1, 3]
```

**Time**: O(n) | **Space**: O(1)

---

## EXAMPLE: 3Sum

```python
def threeSum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result

# Usage
print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
```

**Time**: O(n²) | **Space**: O(1) or O(n) for sorting

---

## EXAMPLE: Container With Most Water

```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)
        
        # Move the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Usage
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
```

**Time**: O(n) | **Space**: O(1)

---

## EXAMPLE: Sort Colors (Dutch National Flag)

```python
def sortColors(nums):
    left = 0
    mid = 0
    right = len(nums) - 1
    
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1

# Usage
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # [0, 0, 1, 1, 2, 2]
```

**Time**: O(n) | **Space**: O(1)

---

## KEY POINTS

✓ Works best on sorted arrays
✓ One pointer from start, one from end
✓ Move based on comparison
✓ Can process triplets with nested pointers
✓ Efficient in-place modifications
✓ No extra space needed
