# def bfs(graph, start):
#     visited = set()  # To keep track of visited vertices
#     queue = []  # To store vertices for processing
#     queue.append(start)
#     visited.add(start)

#     while queue:
#         vertex = queue.pop(0)
#         print(vertex)  # Process the vertex (you can replace this with your own logic)

#         for neighbor in graph[vertex]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 visited.add(neighbor)
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
# bfs(graph, 'A')
class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self,u):
        if u not in self.graph:
            self.graph[u]=[]
    def add_edge(self,u,v):
        if u  in self.graph and v  in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)
def bfs(graph,start):
    visited = set()
    queue = []
    queue.append(start)
    visited.add(start)
    while queue:
        vertex =queue.pop(0)
        print(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
g = Graph()
gr=['A','B','C','D','E','F']
for i in gr:
    g.add_vertex(i)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
bfs(g.graph,'A')
