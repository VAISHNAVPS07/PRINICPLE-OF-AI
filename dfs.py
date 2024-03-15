def DFS(graph, start):
    stack = [start]
    visited = set()

    print("\nOrder of visited nodes by DFS: ", end=" ")

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            print(current_node, end=" ")

            stack.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited)


numeric_graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: []
}

start_node = 5

DFS(numeric_graph, start_node)
