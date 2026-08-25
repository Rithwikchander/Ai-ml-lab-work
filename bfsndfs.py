from collections import deque

def bfs(graph, start):
 visited = set()
 queue=deque([start]) # Corrected typo: dequeue -> deque
 visited.add(start)
 order=[]

 while queue:
  vertex=queue.popleft()
  order.append(vertex)
  for neighbour in graph[vertex]:
   if neighbour not in visited: # Corrected membership check: is not -> not in
     visited.add(neighbour)
     queue.append(neighbour)
 return order

def dfs(graph, start, visited=None, order=None): # Corrected signature for default arguments
   if visited is None: # Corrected typo and case
     visited=set()
   if order is None: # Corrected case
    order = []

   visited.add(start)
   order.append(start)
   for neighbor in graph[start]:
     if neighbor not in visited:
       dfs(graph, neighbor, visited, order)
   return order

#example usage
if __name__== "__main__" :
 #representing graph as an adjacency list
 graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E'],
 }

 print("BFS traversal starting from 'A':", bfs(graph, 'A'))
 print("DFS traversal starting from 'A':", dfs(graph, 'A'))
 
 print("SAMARTH 24BECS140")