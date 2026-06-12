# STACK PATTERN & MONOTONIC STACK

## Pattern Recognition
**Use when you see:**
- Parentheses, brackets validation
- "Next greater element"
- "Previous smaller element"
- Expression evaluation
- LIFO needed

**Red flags**: "Stack", "Parentheses", "Next greater", "Next smaller"

---

## TEMPLATE: Stack - LIFO

```python
stack = []

# Push
stack.append(x)

# Pop
if stack:
    top = stack.pop()

# Peek
if stack:
    top = stack[-1]

# Check empty
if not stack:
    pass
```

---

## TEMPLATE: Monotonic Stack (Increasing)

```python
def next_greater(arr):
    stack = []
    result = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    
    return result
```

---

## TEMPLATE: Valid Parentheses

```python
def isValid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return not stack
```

---

## PROBLEMS YOU CAN SOLVE

1. Valid Parentheses - Check balanced brackets
2. Next Greater Element - Find larger to right
3. Daily Temperatures - Days until warmer
4. Largest Rectangle - Histogram max area
5. Trapping Rain Water - Water trapped
6. Evaluate Postfix - Calculate postfix expr
7. Infix to Postfix - Convert to postfix
8. Stock Span Problem - Consecutive higher
9. Backspace String Compare - With backspace
10. Remove K Digits - Make smallest number
11. Remove Duplicates - Keep lexicographically small
12. Build Array from Permutation

---

## EXAMPLE: Valid Parentheses

```python
def isValid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return not stack

# Usage
print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid("{[}"))  # False
```

**Time**: O(n) | **Space**: O(n)

---

## EXAMPLE: Next Greater Element

```python
def nextGreaterElement(nums):
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    
    return result

# Usage
print(nextGreaterElement([1, 2, 1]))  # [2, -1, -1]
print(nextGreaterElement([1, 2, 3, 4]))  # [2, 3, 4, -1]
```

**Time**: O(n) | **Space**: O(n)

---

## EXAMPLE: Daily Temperatures

```python
def dailyTemperatures(temperatures):
    stack = []  # Indices
    result = [0] * len(temperatures)
    
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
    
    return result

# Usage
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]
```

**Time**: O(n) | **Space**: O(n)

---

## EXAMPLE: Largest Rectangle in Histogram

```python
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h_idx = stack.pop()
            h = heights[h_idx]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    while stack:
        h_idx = stack.pop()
        h = heights[h_idx]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)
    
    return max_area

# Usage
print(largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
```

**Time**: O(n) | **Space**: O(n)

---

## KEY POINTS

✓ LIFO - Last In First Out
✓ Monotonic stack maintains sorted order
✓ Great for "next/previous" problems
✓ Can track indices or values
✓ Perfect for validation problems
✓ Efficient - O(n) even for complex problems
