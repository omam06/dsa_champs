def has_path(graph, start, target):
    visited = set()
    stack = [start] 

    while stack != []:
        node = stack.pop()
        if node == target:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return False

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}
print(has_path(graph, "A", "F"))
print(has_path(graph, "D", "E"))