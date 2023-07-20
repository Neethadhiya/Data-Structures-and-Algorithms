class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self,u):
        if u not in self.graph:
            self.graph[u]=[]
    def add_edge(self, u, v):
        if u not in self.graph and v not in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)
    def dfs(self,start_node):
        visited = set()
        stack = [start_node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node, end=" ")
                if node in self.graph:
                    neighbors = self.graph[node]
                    stack.extend(neighbors)
g = Graph()
gr=['A','B','C','D','E','F']
for i in g:
    g.add_vertex(i)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
print("Depth First Traversal (starting from node 'A'):")
g.dfs('A')