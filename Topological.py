from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        return stack[::-1]

# Example usage:
g = Graph(6)
g.add_edge(1, 2)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(3, 5)

print("Topological Sort:", g.topological_sort())
