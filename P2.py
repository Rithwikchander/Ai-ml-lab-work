#best_first_search

from queue import PriorityQueue

def best_first_search(graph, start, target, heuristics):
    visited = set()
    priority_queue = PriorityQueue()
    # (heuristic_value, current_node, path)
    priority_queue.put((heuristics[start], start, [start]))
    visited.add(start)

    while not priority_queue.empty():
        h, node, path = priority_queue.get()

        if node == target:
            return path, h
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                priority_queue.put((heuristics[neighbor], neighbor, path + [neighbor]))


    return None, None

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    heuristics = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 6,
        'E': 4,
        'F': 0
    }

    start_node = 'A'
    target_node = 'F'
    path, heuristic_value = best_first_search(graph, start_node, target_node, heuristics)

    if path:
        print(f"Best First Search Path from {start_node} to {target_node}: {path} \n heuristic value: {heuristic_value}")
    else:
        print(f"No path found from {start_node} to {target_node}.")