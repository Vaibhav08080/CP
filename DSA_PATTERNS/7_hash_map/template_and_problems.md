# HASH MAP PATTERN

## Pattern Recognition
**Use when you see:**
- Frequency counting
- "First", "Find duplicates"
- Mapping/pairing elements
- Two numbers operations
- Grouping by property

**Red flags**: "Duplicates", "Frequency", "Count", "Unique", "Pairing"

---

## TEMPLATE: Frequency Counting

```python
def frequency_count(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    return freq
```

---

## TEMPLATE: Find Pair with Property

```python
def find_pair(arr, target):
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    
    return []
```

---

## TEMPLATE: Character Frequency

```python
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    return freq
```

---

## PROBLEMS YOU CAN SOLVE

1. Two Sum - Find pair with sum
2. Contains Duplicate - Check duplicates
3. Valid Anagram - Rearrangement check
4. Group Anagrams - Group by anagram
5. Top K Frequent Elements - Most common k
6. Majority Element - > n/2 element
7. First Unique Character - First non-repeat
8. Ransom Note - Can construct from letters
9. Happy Number - Cycle detection
10. LRU Cache - Least Recently Used
11. Isomorphic Strings - Pattern mapping
12. Word Pattern - Pattern matching

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

## EXAMPLE: Group Anagrams

```python
def groupAnagrams(strs):
    anagrams = {}
    
    for s in strs:
        key = tuple(sorted(s))  # Or use char count
        
        if key not in anagrams:
            anagrams[key] = []
        
        anagrams[key].append(s)
    
    return list(anagrams.values())

# Usage
print(groupAnagrams(["eat", "tea", "ate", "eat", "tan", "ate", "nat"]))
# [["eat", "tea", "ate", "eat", "ate"], ["tan", "nat"]]
```

**Time**: O(n * k log k) | **Space**: O(n*k)

---

## EXAMPLE: Top K Frequent Elements

```python
from collections import Counter
import heapq

def topKFrequent(nums, k):
    # Method 1: Using Counter and heap
    freq = Counter(nums)
    return heapq.nlargest(k, freq, key=freq.get)

# Method 2: Using heap
def topKFrequent_v2(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    return heapq.nlargest(k, freq, key=freq.get)

# Usage
print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
```

**Time**: O(n log k) | **Space**: O(n)

---

## EXAMPLE: First Unique Character

```python
def firstUniqChar(s):
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1

# Usage
print(firstUniqChar("leetcode"))  # 0 ('l' appears once first)
print(firstUniqChar("loveleetcode"))  # 2 ('v' is first unique)
```

**Time**: O(n) | **Space**: O(1) (max 26 chars)

---

## EXAMPLE: Valid Anagram

```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    freq_s = {}
    freq_t = {}
    
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1
    
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    
    return freq_s == freq_t

# Better: using Counter
from collections import Counter
def isAnagram_v2(s, t):
    return Counter(s) == Counter(t)

# Usage
print(isAnagram("anagram", "nagaram"))  # True
```

**Time**: O(n) | **Space**: O(1)

---

## KEY POINTS

✓ Great for frequency/counting problems
✓ Use dict for ordering, set for uniqueness
✓ combine with heap for top k
✓ Use sorted key or char count for anagrams
✓ O(1) average access time
✓ Perfect for pairing problems
✓ Consider Counter from collections
