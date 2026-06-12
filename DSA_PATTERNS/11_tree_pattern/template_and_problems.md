# TREE PATTERN

## Pattern Recognition
**Use when you see:**
- Tree traversal (inorder, preorder, postorder)
- Tree path problems
- Tree modification/construction
- "Depth", "Height", "Balanced"
- Recursive tree structure

**Red flags**: "Tree", "Inorder", "Path", "LCA", "Balanced", "Height"

---

## TEMPLATE: Tree Node

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## TEMPLATE: Inorder Traversal (Left-Root-Right)

```python
def inorder(root):
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result
```

---

## TEMPLATE: Tree Recursion Pattern

```python
def tree_operation(root):
    if not root:
        return base_case
    
    left_result = tree_operation(root.left)
    right_result = tree_operation(root.right)
    
    return combine(left_result, right_result, root.val)
```

---

## PROBLEMS YOU CAN SOLVE

1. Inorder Traversal - Left-Root-Right
2. Preorder Traversal - Root-Left-Right
3. Postorder Traversal - Left-Right-Root
4. Level Order - BFS traversal
5. Max Path Sum - Largest path sum
6. Path Sum - Path equals target
7. Validate BST - Check valid BST
8. Lowest Common Ancestor - LCA of nodes
9. Diameter - Longest path
10. Balanced Tree - Check if balanced
11. Serialize/Deserialize - Convert to string
12. Invert Tree - Mirror the tree

---

## EXAMPLE: Inorder Traversal

```python
def inorderTraversal(root):
    result = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result

# Iterative version
def inorderTraversal_iterative(root):
    result = []
    stack = []
    node = root
    
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        result.append(node.val)
        node = node.right
    
    return result

# Usage
#     1
#    / \
#   2   3
# Returns [2, 1, 3]
```

**Time**: O(n) | **Space**: O(h)

---

## EXAMPLE: Maximum Path Sum

```python
def maxPathSum(root):
    max_sum = float('-inf')
    
    def dfs(node):
        nonlocal max_sum
        
        if not node:
            return 0
        
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        
        # Max path through this node
        path_sum = left + right + node.val
        max_sum = max(max_sum, path_sum)
        
        # Return max path ending at this node
        return max(left, right) + node.val
    
    dfs(root)
    return max_sum

# Usage
#        1
#       / \
#      2   3
# Returns 6 (2 + 1 + 3)
```

**Time**: O(n) | **Space**: O(h)

---

## EXAMPLE: Lowest Common Ancestor

```python
def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    
    if root.val == p.val or root.val == q.val:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right

# Usage - returns LCA node
```

**Time**: O(n) | **Space**: O(h)

---

## EXAMPLE: Validate BST

```python
def isValidBST(root):
    def dfs(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (dfs(node.left, min_val, node.val) and
                dfs(node.right, node.val, max_val))
    
    return dfs(root, float('-inf'), float('inf'))

# Usage
```

**Time**: O(n) | **Space**: O(h)

---

## KEY POINTS

✓ Tree inherently recursive
✓ Preorder: process before children
✓ Inorder: process between children
✓ Postorder: process after children
✓ Level order: use BFS
✓ Common to combine with DFS/BFS
✓ Track min/max for BST validation
✓ Use recursion stack for space
