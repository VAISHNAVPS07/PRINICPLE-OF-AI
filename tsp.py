import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    def heuristic(self, v, visited, count):
        remaining_nodes = 0
        for i in range(self.V):
            if visited[i] == False:
                remaining_nodes += 1
        return remaining_nodes

    def tsp(self):
        pq = []
        src = 0
        visited = [False] * self.V
        visited[src] = True
        initial_path_cost = 0
        level = 0
        heappush(pq, (initial_path_cost, level, src, visited))
        while pq:
            path_cost, level, curr, visited = heappop(pq)
            if level == self.V - 1:
                return path_cost + self.graph[curr][src]
            for i in range(self.V):
                if visited[i] == False:
                    current_path_cost = path_cost + self.graph[curr][i]
                    heuristic_value = self.heuristic(i, visited, level)
                    total_cost = current_path_cost + heuristic_value
                    new_visited = visited[:]
                    new_visited[i] = True
                    heappush(pq, (current_path_cost, level + 1, i, new_visited))
        return -1

# Example usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 15)
g.add_edge(0, 3, 20)
g.add_edge(1, 2, 35)
g.add_edge(1, 3, 25)
g.add_edge(2, 3, 30)
print("Minimum cost:", g.tsp())
