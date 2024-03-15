from collections import deque

def BFS(graph, start):
    queue = deque([start])
    visited = set()

    print("\nOrder of visited nodes by BFS: ", end=" ")

    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            visited.add(current_node)
            print(current_node, end=" ")

            queue.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited)

numeric_graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: []
}

start_node = 5

BFS(numeric_graph, start_node)
