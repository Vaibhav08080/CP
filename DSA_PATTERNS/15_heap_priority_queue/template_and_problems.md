# HEAP & PRIORITY QUEUE PATTERN

## Pattern Recognition
**Use when you see:**
- "Top k", "Largest/smallest"
- "Median finding"
- "Frequency ordering"
- Task scheduling
- Stream problems

**Red flags**: "Heap", "Priority", "Top K", "Median", "Frequent"

---

## TEMPLATE: Min Heap

```python
import heapq

# Create min heap
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)

# Pop minimum
min_val = heapq.heappop(heap)

# Create from list
heap = [3, 1, 5, 2]
heapq.heapify(heap)

# Get top k
top_k = heapq.nsmallest(2, heap)
```

---

## TEMPLATE: Max Heap (Using Min Heap)

```python
import heapq

# For max heap, negate values
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)

max_val = -heapq.heappop(max_heap)
```

---

## TEMPLATE: K Largest Elements

```python
import heapq

def find_k_largest(nums, k):
    return heapq.nlargest(k, nums)

# Or with min-heap of size k
def find_k_largest_v2(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap
```

---

## PROBLEMS YOU CAN SOLVE

1. Top K Frequent Elements - K most common
2. Find Median - Stream median
3. K Closest Points - K nearest
4. Merge K Sorted - Merge lists
5. Reorganize String - Rearrange chars
6. Task Scheduler - With cooldown
7. Furthest Building - Climb building
8. IPO - Max capital after projects
9. Minimum Cost to Connect - Min cost
10. Last Stone Weight - Remove stones
11. K Smallest Elements - K smallest
12. Meeting Rooms II - Min rooms

---

## EXAMPLE: Top K Frequent Elements

```python
from collections import Counter
import heapq

def topKFrequent(nums, k):
    if k == len(nums):
        return nums
    
    freq = Counter(nums)
    return heapq.nlargest(k, freq, key=freq.get)

# Alternative: Using min-heap
def topKFrequent_v2(nums, k):
    freq = Counter(nums)
    heap = []
    
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for count, num in heap]

# Usage
print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
```

**Time**: O(n log k) | **Space**: O(k)

---

## EXAMPLE: Find Median from Data Stream

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negated)
        self.large = []  # Min heap
        self.small_size = 0
        self.large_size = 0
    
    def addNum(self, num):
        if self.small_size == self.large_size:
            if self.large and num > self.large[0]:
                heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
            else:
                heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            if num < -self.small[0]:
                heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
            else:
                heapq.heappush(self.large, num)
            self.large_size += 1
    
    def findMedian(self):
        if self.small_size > self.large_size:
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

# Usage
mf = MedianFinder()
mf.addNum(1)
print(mf.findMedian())  # 1
mf.addNum(2)
print(mf.findMedian())  # 1.5
```

**Time**: O(log n) per add | **Space**: O(n)

---

## EXAMPLE: Merge K Sorted Lists

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    
    # Push first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode()
    current = dummy
    
    while heap:
        val, idx, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    
    return dummy.next

# Usage
```

**Time**: O(n log k) | **Space**: O(k)

---

## KEY POINTS

✓ Min heap by default in Python
✓ Negate for max heap behavior
✓ Maintain size constraint for top k
✓ Great for streaming problems
✓ O(1) access to best element
✓ O(log n) insert/remove
✓ Use heapify to convert list to heap
