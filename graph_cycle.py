def has_cycle(graph):
    visited = set()     
    rec_stack = set()   
    
    def dfs(node):
        if node in rec_stack:
            return True
        if node in visited:
            return False

        rec_stack.add(node)
        visited.add(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}
print(has_cycle(graph))  
