# MATRIX PATTERN

## Pattern Recognition
**Use when you see:**
- 2D grid problems
- "Search in matrix", "Spiral"
- "Rotate", "Set zeroes"
- Boundary traversal
- "Valid sudoku"

**Red flags**: "Matrix", "Grid", "2D", "Rows/columns", "Boundaries"

---

## TEMPLATE: Matrix Traversal

```python
def traverse_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            # Process matrix[i][j]
            pass
```

---

## TEMPLATE: DFS in Matrix

```python
def dfs_matrix(matrix, i, j, visited):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return
    if visited[i][j]:
        return
    
    visited[i][j] = True
    
    # Explore 4 directions
    dfs_matrix(matrix, i+1, j, visited)
    dfs_matrix(matrix, i-1, j, visited)
    dfs_matrix(matrix, i, j+1, visited)
    dfs_matrix(matrix, i, j-1, visited)
```

---

## TEMPLATE: Spiral Order

```python
def spiral_order(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        # Up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result
```

---

## PROBLEMS YOU CAN SOLVE

1. Number of Islands - Count connected regions
2. Search Word in Matrix - Find word path
3. Spiral Order - Spiral traversal
4. Set Matrix Zeroes - Set rows/cols to 0
5. Rotate Matrix - 90 degree rotation
6. Maximal Rectangle - Largest rectangle
7. Shortest Path - In grid
8. Pacific Atlantic - Water flow
9. Valid Sudoku - Check sudoku
10. Strobogrammatic Numbers - Special numbers
11. Word Ladder II - All paths
12. Alien Dictionary - Letter ordering

---

## EXAMPLE: Number of Islands

```python
def numIslands(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    count = 0
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if visited[i][j] or grid[i][j] == '0':
            return
        
        visited[i][j] = True
        
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(i, j)
                count += 1
    
    return count

# Usage
grid = [['1', '1', '0'], ['0', '1', '0'], ['1', '0', '1']]
print(numIslands(grid))  # 3
```

**Time**: O(m*n) | **Space**: O(m*n)

---

## EXAMPLE: Spiral Order

```python
def spiralOrder(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Traverse left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        # Traverse up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

# Usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix))  # [1,2,3,6,9,8,7,4,5]
```

**Time**: O(m*n) | **Space**: O(1)

---

## EXAMPLE: Rotate Matrix

```python
def rotate(matrix):
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

**Time**: O(m*n) | **Space**: O(1)

---

## KEY POINTS

✓ 4 directions: right, down, left, up
✓ Check boundaries before accessing
✓ Track visited to avoid cycles
✓ Can modify matrix or use visited array
✓ Boundary pointers for spiral
✓ Transpose + reverse = 90° rotation
✓ Common in interview questions
