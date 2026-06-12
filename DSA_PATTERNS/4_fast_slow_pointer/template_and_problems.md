# FAST & SLOW POINTER PATTERN

## Pattern Recognition
**Use when you see:**
- Cycle detection in linked list
- Finding middle element
- Linked list manipulation
- "Slow pointer", "Fast pointer"
- "Cycle", "Middle node"

**Red flags**: "Linked list", "Cycle", "Middle", "kth position"

---

## TEMPLATE: Cycle Detection

```python
def has_cycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
```

---

## TEMPLATE: Find Middle

```python
def find_middle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # Middle node
```

---

## TEMPLATE: Find Cycle Start

```python
def find_cycle_start(head):
    slow = fast = head
    
    # Find cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    # Find start
    ptr1 = head
    ptr2 = slow
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1
```

---

## PROBLEMS YOU CAN SOLVE

1. Linked List Cycle - Detect cycle exists
2. Linked List Cycle II - Find cycle start node
3. Middle of Linked List - Find middle element
4. Happy Number - Cycle in digit sum
5. Palindrome Linked List - Check if palindrome
6. Remove Nth Node - From end of list
7. Reorder List - Rearrange L1->L2->L3 pattern
8. Rotate List - Rotate by k positions
9. Intersection of Linked Lists - Find intersection
10. Start of Cycle - Exact starting node
11. Linked List Components - Count components
12. Reverse Nodes in K Group - Reverse in groups

---

## EXAMPLE: Linked List Cycle Detection

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True

# Usage
# Create: 1 -> 2 -> 3 -> 4 -> 2 (cycle to 2)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next  # Create cycle

print(hasCycle(head))  # True
```

**Time**: O(n) | **Space**: O(1)

---

## EXAMPLE: Find Cycle Start Node

```python
def detectCycle(head):
    if not head or not head.next:
        return None
    
    slow = fast = head
    
    # Find intersection point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if not fast or not fast.next:
        return None  # No cycle
    
    # Find cycle start
    ptr1 = head
    ptr2 = slow
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1

# Usage - returns the node where cycle starts
```

**Time**: O(n) | **Space**: O(1)

---

## EXAMPLE: Middle of Linked List

```python
def middleNode(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # Middle node

# Usage
# 1 -> 2 -> 3 -> 4 -> 5
# Returns node 3

# 1 -> 2 -> 3 -> 4
# Returns node 3
```

**Time**: O(n) | **Space**: O(1)

---

## EXAMPLE: Happy Number (Cycle Detection in Numbers)

```python
def isHappy(n):
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10
        return total
    
    slow = n
    fast = get_next(n)
    
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast == 1

# Usage
print(isHappy(7))  # True
print(isHappy(2))  # False
```

**Time**: O(log n) | **Space**: O(1)

---

## KEY POINTS

✓ Two pointer speeds: slow (1x), fast (2x)
✓ If cycle exists, they will meet
✓ For finding cycle start: reset one pointer to head
✓ Works for linked lists and number patterns
✓ Very space efficient - no extra data structure
✓ Common in interview questions
