#implementation of BFS and DFS



from asyncio import graph
from collections import deque

from matplotlib.pylab import stack

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph.get(current, []): 
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))

    return result

#Example usage

if __name__ == "__main__":

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS Traversal starting from vertex A:", bfs(graph, 'A'))
    print("DFS Traversal starting from vertex A:", dfs(graph, 'A'))