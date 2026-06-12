# BIT MANIPULATION PATTERN

## Pattern Recognition
**Use when you see:**
- Single number problems
- "Power of 2"
- "Bit operations"
- XOR properties needed
- Bit flags/masks

**Red flags**: "Bit", "XOR", "AND", "OR", "Shift", "Binary"

---

## COMMON BIT OPERATIONS

```python
# AND: Both bits 1
a & b

# OR: At least one bit 1
a | b

# XOR: Bits different
a ^ b

# NOT: Flip bits
~a

# Left shift: Multiply by 2
a << 1

# Right shift: Divide by 2
a >> 1

# Check if bit i is set
(a >> i) & 1

# Set bit i
a | (1 << i)

# Clear bit i
a & ~(1 << i)

# Toggle bit i
a ^ (1 << i)

# Check power of 2
(n & (n - 1)) == 0

# Count set bits
bin(n).count('1')
```

---

## TEMPLATE: Count Set Bits

```python
def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

---

## TEMPLATE: Single Number (XOR)

```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

---

## PROBLEMS YOU CAN SOLVE

1. Single Number - Find unique element
2. Single Number II - Appear 3 times
3. Single Number III - Two unique
4. Missing Number - Find missing
5. Power of Two - Check if power of 2
6. Hamming Distance - Bit differences
7. Number of 1 Bits - Count bits
8. Reverse Bits - Mirror binary
9. Sum of Two Integers - Without +/-
10. Bitwise AND of Range - AND all in range
11. UTF-8 Validation - Check valid
12. Maximum Product of Word Lengths

---

## EXAMPLE: Single Number

```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR with all
    return result

# Why? XOR properties:
# a ^ a = 0
# a ^ 0 = a
# XOR is commutative and associative
# So all pairs cancel out, leaving single

# Usage
print(singleNumber([4, 1, 2, 1, 2]))  # 4
print(singleNumber([2, 2, 1]))  # 1
```

**Time**: O(n) | **Space**: O(1)

---

## EXAMPLE: Hamming Distance

```python
def hammingDistance(x, y):
    xor_result = x ^ y
    distance = 0
    
    while xor_result:
        distance += xor_result & 1
        xor_result >>= 1
    
    return distance

# Or simpler
def hammingDistance_v2(x, y):
    return bin(x ^ y).count('1')

# Usage
print(hammingDistance(1, 4))  # 2 (1=001, 4=100, diff at 2 places)
```

**Time**: O(log n) | **Space**: O(1)

---

## EXAMPLE: Power of Two

```python
def isPowerOfTwo(n):
    if n <= 0:
        return False
    
    # n & (n-1) removes rightmost 1
    # Power of 2 has only one 1 bit
    return (n & (n - 1)) == 0

# Usage
print(isPowerOfTwo(1))  # True (2^0)
print(isPowerOfTwo(16))  # True (2^4)
print(isPowerOfTwo(3))  # False
```

**Time**: O(1) | **Space**: O(1)

---

## EXAMPLE: Number of 1 Bits

```python
def hammingWeight(n):
    count = 0
    while n:
        count += n & 1  # Check rightmost bit
        n >>= 1  # Right shift
    return count

# Or using built-in
def hammingWeight_v2(n):
    return bin(n).count('1')

# Usage
print(hammingWeight(11))  # 3 (1011 has 3 ones)
```

**Time**: O(log n) | **Space**: O(1)

---

## EXAMPLE: Missing Number

```python
def missingNumber(nums):
    n = len(nums)
    
    # Method 1: XOR
    result = 0
    for i in range(n + 1):
        result ^= i
    for num in nums:
        result ^= num
    return result
    
    # Method 2: Math
    # return n * (n + 1) // 2 - sum(nums)

# Usage
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
```

**Time**: O(n) | **Space**: O(1)

---

## KEY POINTS

✓ XOR: a ^ a = 0, a ^ 0 = a
✓ AND: Get common bits
✓ OR: Combine bits
✓ Shift: Efficient multiply/divide
✓ Bit mask: Track multiple flags
✓ n & (n-1): Remove rightmost 1
✓ Perfect for optimization
✓ Often O(1) space
