graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'],
    'C': ['F'], 'D': ['G'], 'E': ['G'],
    'F': ['G'], 'G': []
}

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                queue.append(path + [child])
    return None

print("BFS path:", bfs('A', 'G'))