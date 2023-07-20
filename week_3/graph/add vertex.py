class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self,node):
        if node not in self.graph:
            self.graph[node]=[]
    def add_edge(self,node1,node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
    def display(self):
        # for i,j in self.graph.items():
        #     print(i,"->",j)
        for node in self.graph:
            print(node,"->",self.graph[node])
        print(self.graph)
graph = Graph()
g=['A','B','C','D','E']
for i in g:
    graph.add_vertex(i)
# graph.add_vertex("A")
# graph.add_vertex("B")
# graph.add_vertex("C")
# graph.add_vertex("D")
graph.add_edge("A","B")
graph.add_edge("B","C")
graph.add_edge("B","D")
graph.display()

