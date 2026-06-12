# GREEDY PATTERN

## Pattern Recognition
**Use when you see:**
- "Maximum", "Minimum" without complex dependency
- Sorting + selection
- Local optimal choice
- Activity/interval scheduling
- No backtracking needed

**Red flags**: "Greedy", "Maximize", "Minimize", "Select", "Sort"

---

## TEMPLATE: Sort and Select

```python
def greedy_sort_select(arr):
    # Sort by criteria
    arr.sort(key=lambda x: x[1])  # Or custom key
    
    result = []
    for item in arr:
        if is_feasible(result, item):
            result.append(item)
    
    return result
```

---

## TEMPLATE: Activity Selection

```python
def activity_selection(activities):
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    
    for i in range(1, len(activities)):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])
    
    return selected
```

---

## PROBLEMS YOU CAN SOLVE

1. Activity Selection - Non-overlapping
2. Jump Game - Can reach end
3. Container With Most Water - Max area
4. Lemonade Change - Give correct change
5. Interval Scheduling - Maximum non-overlapping
6. Gas Station - Complete circuit
7. Assign Cookies - Satisfy kids
8. Two City Scheduling - Min cost
9. Majority Element - >n/2 element
10. Best Time to Buy Stock - Max profit
11. Fractional Knapsack - Value/weight
12. Meeting Rooms - Min rooms

---

## EXAMPLE: Jump Game

```python
def canJump(nums):
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + nums[i])
    
    return True

# Usage
print(canJump([2, 3, 1, 1, 4]))  # True
print(canJump([3, 2, 1, 0, 4]))  # False
```

**Time**: O(n) | **Space**: O(1)

---

## EXAMPLE: Container With Most Water

```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)
        
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

## EXAMPLE: Activity Selection

```python
def activitySelection(activities):
    # activities: [(name, start, end), ...]
    activities.sort(key=lambda x: x[2])
    
    selected = [activities[0]]
    
    for i in range(1, len(activities)):
        if activities[i][1] >= selected[-1][2]:
            selected.append(activities[i])
    
    return selected

# Usage
activities = [('A', 1, 2), ('B', 3, 4), ('C', 0, 6)]
print(activitySelection(activities))
```

**Time**: O(n log n) | **Space**: O(n)

---

## EXAMPLE: Gas Station

```python
def canCompleteCircuit(gas, cost):
    total_gas = 0
    current_gas = 0
    start = 0
    
    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]
        
        if current_gas < 0:
            start = i + 1
            current_gas = 0
    
    return start if total_gas >= 0 else -1

# Usage
print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # 3
```

**Time**: O(n) | **Space**: O(1)

---

## KEY POINTS

✓ Make locally optimal choice
✓ Hope it leads to globally optimal
✓ Greedy doesn't always work - verify!
✓ Often requires sorting first
✓ Usually very efficient
✓ Compare with DP if unsure
✓ Test with examples first
