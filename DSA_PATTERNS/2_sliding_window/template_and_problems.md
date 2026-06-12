# SLIDING WINDOW PATTERN

## Pattern Recognition
**Use when you see:**
- Fixed/dynamic window size
- Substring/subarray problems
- "Minimum length", "Maximum sum" in subarray
- Contiguous element problems

**Red flags**: "Contiguous", "Window", "Substring", "At most/least"

---

## TEMPLATE: Fixed Window

```python
def fixed_window(arr, k):
    # Calculate sum/operation for first window
    window = sum(arr[:k])
    result = window
    
    # Slide the window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]  # Remove left, add right
        result = max(result, window)  # Or process as needed
    
    return result
```

---

## TEMPLATE: Dynamic Window (Two Pointer)

```python
def dynamic_window(s, target):
    left = 0
    current = 0
    result = float('inf')
    
    for right in range(len(s)):
        current += s[right]
        
        while current >= target:
            result = min(result, right - left + 1)
            current -= s[left]
            left += 1
    
    return result if result != float('inf') else 0
```

---

## TEMPLATE: Character Count Window

```python
def char_window(s, t):
    if not t:
        return ""
    
    window = {}
    required = {}
    for c in t:
        required[c] = required.get(c, 0) + 1
    
    left = formed = 0
    result = float('inf'), 0, 0
    
    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        if char in required and window[char] == required[char]:
            formed += 1
        
        while formed == len(required):
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            
            left_char = s[left]
            window[left_char] -= 1
            if left_char in required and window[left_char] < required[left_char]:
                formed -= 1
            left += 1
    
    return s[result[1]:result[2] + 1] if result[0] != float('inf') else ""
```

---

## PROBLEMS YOU CAN SOLVE

1. Maximum Subarray Sum - Kadane's algorithm
2. Longest Substring Without Repeating - Unique chars
3. Minimum Window Substring - Find smallest substring
4. Permutation in String - Check if permutation exists
5. Sliding Window Maximum - Max in every window
6. Longest Repeating Character Replacement - After replacements
7. Max Consecutive Ones - Max 1s after flips
8. Fruit Into Baskets - At most 2 types
9. Longest Substring with K Distinct - K unique chars
10. Smallest Range - From k lists
11. Number of Substrings - With all unique chars
12. Equal Subarray - After replacing K

---

## EXAMPLE: Longest Substring Without Repeating

```python
def lengthOfLongestSubstring(s):
    char_index = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Usage
print(lengthOfLongestSubstring("abcabcbb"))  # 3 ("abc")
print(lengthOfLongestSubstring("bbbbb"))  # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))  # 3 ("wke")
```

**Time**: O(n) | **Space**: O(min(n, charset))

---

## EXAMPLE: Sliding Window Maximum

```python
from collections import deque

def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []
    
    dq = deque()  # Stores indices
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Usage
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
```

**Time**: O(n) | **Space**: O(k)

---

## EXAMPLE: Minimum Window Substring

```python
def minWindow(s, t):
    if not s or not t:
        return ""
    
    required = {}
    for c in t:
        required[c] = required.get(c, 0) + 1
    
    window = {}
    formed = 0
    left = 0
    result = float('inf'), 0, 0
    
    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        if char in required and window[char] == required[char]:
            formed += 1
        
        while formed == len(required):
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            
            left_char = s[left]
            window[left_char] -= 1
            if left_char in required and window[left_char] < required[left_char]:
                formed -= 1
            left += 1
    
    return s[result[1]:result[2] + 1] if result[0] != float('inf') else ""

# Usage
print(minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
print(minWindow("a", "a"))  # "a"
```

**Time**: O(n + m) | **Space**: O(charset)

---

## KEY POINTS

✓ Move right pointer to expand window
✓ Move left pointer to contract when condition met
✓ Track what you need in dict/counter
✓ Update result when valid window found
✓ Optimize by knowing when to shrink
