# DFS & BACKTRACKING PATTERN

## Pattern Recognition
**Use when you see:**
- Tree/graph traversal
- "All combinations", "All permutations"
- "Explore all possibilities"
- "Find all paths"
- Recursive structure

**Red flags**: "DFS", "Backtrack", "All solutions", "Permutation", "Combination"

---

## TEMPLATE: Basic DFS (Recursive)

```python
def dfs(node, visited, graph):
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)
```

---

## TEMPLATE: DFS Iterative

```python
def dfs_iterative(start, graph):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
```

---

## TEMPLATE: Backtracking

```python
def backtrack(path, candidates, result):
    if is_valid(path):
        result.append(path[:])
        return
    
    for candidate in candidates:
        path.append(candidate)
        if is_feasible(path):
            backtrack(path, candidates, result)
        path.pop()  # Backtrack
```

---

## PROBLEMS YOU CAN SOLVE

1. Number of Islands - Count connected
2. Permutations - All orderings
3. Combinations - All subsets of size k
4. Subsets - All subsets
5. Word Search - Find word in grid
6. Sudoku Solver - Fill sudoku
7. N-Queens - Place n queens
8. Generate Parentheses - Valid combos
9. Path Sum - Root to leaf equals sum
10. All Paths - All paths in tree
11. Letter Combinations - Phone keypad
12. Restore IP Addresses - Valid IPs

---

## EXAMPLE: Number of Islands

```python
def numIslands(grid):
    if not grid:
        return 0
    
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] != '1':
            return
        
        grid[i][j] = '0'  # Mark visited
        
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                islands += 1
    
    return islands

# Usage
grid = [['1', '1', '0'], ['0', '1', '0'], ['1', '0', '1']]
print(numIslands(grid))  # 3
```

**Time**: O(m*n) | **Space**: O(m*n)

---

## EXAMPLE: Permutations

```python
def permute(nums):
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    
    backtrack([], nums)
    return result

# Usage
print(permute([1, 2, 3]))
# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

**Time**: O(n! * n) | **Space**: O(n!)

---

## EXAMPLE: Combinations

```python
def combine(n, k):
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(1, [])
    return result

# Usage
print(combine(4, 2))  # [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
```

**Time**: O(C(n,k) * k) | **Space**: O(C(n,k))

---

## EXAMPLE: Generate Parentheses

```python
def generateParenthesis(n):
    result = []
    
    def backtrack(path, open_count, close_count):
        if len(path) == 2 * n:
            result.append(path)
            return
        
        if open_count < n:
            backtrack(path + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(path + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result

# Usage
print(generateParenthesis(3))
# ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

**Time**: O(4^n) | **Space**: O(n)

---

## KEY POINTS

✓ DFS goes deep first
✓ Backtracking explores all paths
✓ Mark as visited to avoid cycles
✓ Restore state when backtracking (path.pop())
✓ Great for finding all solutions
✓ Can be recursive or iterative
