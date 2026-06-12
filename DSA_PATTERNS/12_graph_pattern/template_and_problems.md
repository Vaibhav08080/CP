# GRAPH PATTERN

## Pattern Recognition
**Use when you see:**
- Multiple nodes with relationships
- Path finding, connectivity
- "Shortest distance", "Minimum cost"
- Topological ordering
- Cycle detection

**Red flags**: "Graph", "Nodes", "Edges", "Path", "Connected"

---

## TEMPLATE: Adjacency List Graph

```python
# Build graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Or with weights
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2)],
    'D': [('B', 2)]
}
```

---

## TEMPLATE: Dijkstra's Algorithm

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

---

## TEMPLATE: Topological Sort (Kahn's Algorithm)

```python
from collections import deque

def topologicalSort(graph, vertices):
    in_degree = {v: 0 for v in vertices}
    
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([v for v in vertices if in_degree[v] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result
```

---

## PROBLEMS YOU CAN SOLVE

1. Number of Connected Components - Find components
2. Shortest Path (Weighted) - Dijkstra's
3. Topological Sort - DAG ordering
4. Detect Cycle - Find cycle
5. Course Schedule - Prerequisites order
6. Network Delay - Min time to reach
7. Arbitrage - Currency exchange
8. Alien Dictionary - Letter order
9. Reconstruct Itinerary - Flight path
10. Swim in Rising Water - Minimize effort
11. Minimum Spanning Tree - MST
12. Strongly Connected Components - SCC

---

## EXAMPLE: Dijkstra's Algorithm

```python
import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    parents = {node: None for node in graph}
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph.get(current, []):
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    
    return distances[end], path

# Usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

dist, path = dijkstra(graph, 'A', 'D')
print(f"Distance: {dist}, Path: {path}")  # Distance: 4, Path: ['A', 'B', 'C', 'D']
```

**Time**: O((V+E) log V) | **Space**: O(V)

---

## EXAMPLE: Topological Sort

```python
from collections import deque, defaultdict

def topologicalSort(courses, prerequisites):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for course in courses:
        if course not in in_degree:
            in_degree[course] = 0
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([course for course in courses if in_degree[course] == 0])
    result = []
    
    while queue:
        course = queue.popleft()
        result.append(course)
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return result if len(result) == len(courses) else []

# Usage - returns order to take courses
```

**Time**: O(V + E) | **Space**: O(V + E)

---

## EXAMPLE: Detect Cycle

```python
def hasCycle(graph):
    visited = set()
    rec_stack = set()
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    
    return False

# Usage
```

**Time**: O(V + E) | **Space**: O(V)

---

## KEY POINTS

✓ Adjacency list efficient for sparse graphs
✓ Dijkstra for weighted paths
✓ Topological sort for DAG
✓ DFS for cycle detection
✓ BFS for shortest unweighted path
✓ Use heap/priority queue for optimization
✓ Track visited and in_degree
