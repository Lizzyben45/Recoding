def path_exists(graph, start, target):
    if start == target:
        return True

    queue = [start]
    visited = {start}

    while queue:
        current_node = queue.pop(0)

        for neighbour in graph.get(current_node, []):
            if neighbour == target:
                return True

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return True

graph = {
    "A": ["B","C"],
    "B": ["D"],
    "C": ["E"],
    "E": ["F"],
    "F": []
}  

print("path from A to F exists:",path_exists(graph, start="A", target="F")) 
print("path from D to A exists:",path_exists(graph, start="D", target="A"))                                   