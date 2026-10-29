def shortest_path(graph, start, target):
    if start == target:
        return [start]
        
    queue = [(start, [start])]
    
    visited = {start}
    
    while queue:
        current, path = queue.pop(0)
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                if neighbor == target:
                    return path + [neighbor]
                
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

print(shortest_path(graph, "A", "F"))
