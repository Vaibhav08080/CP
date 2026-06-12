# BFS & LEVEL ORDER PATTERN

## Pattern Recognition
**Use when you see:**
- Shortest path problems
- Level-by-level processing
- Tree level order
- "Minimum steps", "Shortest distance"
- Multi-source problems

**Red flags**: "BFS", "Level order", "Shortest", "Minimum distance"

---

## TEMPLATE: Basic BFS

```python
from collections import deque

def bfs(start, graph):
    visited = {start}
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

---

## TEMPLATE: Level Order Traversal

```python
from collections import deque

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

---

## TEMPLATE: Shortest Path

```python
from collections import deque

def shortest_path(start, end, graph):
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []
```

---

## PROBLEMS YOU CAN SOLVE

1. Level Order Traversal - Tree levels
2. Shortest Path - Unweighted graph
3. Binary Tree Zigzag - Zigzag levels
4. Rotting Oranges - Multi-source BFS
5. Word Ladder - Shortest transformation
6. Number of Islands - Connected components
7. Perfect Squares - Min squares to sum
8. Walls and Gates - Distance from gate
9. Course Schedule - Cycle detection
10. Connected Components - Find all
11. Minimum Knight Moves - Chessboard
12. Furthest Building - Greedy with BFS

---

## EXAMPLE: Level Order Traversal

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Usage
#       3
#      / \
#     9  20
#       /  \
#      15   7
# Returns [[3], [9, 20], [15, 7]]
```

**Time**: O(n) | **Space**: O(w) where w is max width

---

## EXAMPLE: Rotting Oranges

```python
from collections import deque

def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    # Find all rotten oranges
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    
    if fresh == 0:
        return 0
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    time = 0
    
    while queue:
        i, j, time = queue.popleft()
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                queue.append((ni, nj, time + 1))
                fresh -= 1
    
    return time if fresh == 0 else -1

# Usage
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(orangesRotting(grid))  # 4
```

**Time**: O(m*n) | **Space**: O(m*n)

---

## EXAMPLE: Word Ladder

```python
from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    
    if endWord not in wordSet:
        return 0
    
    queue = deque([(beginWord, 1)])
    visited = {beginWord}
    
    while queue:
        word, steps = queue.popleft()
        
        if word == endWord:
            return steps
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                
                if new_word in wordSet and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    
    return 0

# Usage
print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
```

**Time**: O(n*l*26) | **Space**: O(n)

---

## KEY POINTS

✓ BFS explores level by level
✓ FIFO - First In First Out
✓ Perfect for shortest path (unweighted)
✓ Track visited to avoid cycles
✓ Multi-source: start with multiple nodes
✓ Use deque for efficiency
✓ Time usually O(V + E)
