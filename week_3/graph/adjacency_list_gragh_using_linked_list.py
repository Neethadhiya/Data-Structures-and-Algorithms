class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = None

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)

    def add_edge(self, value1, value2):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)
        if node1 is not None and node2 is not None:
            if node1.neighbors is None:
                node1.neighbors = Node(node2)
            else:
                current = node1.neighbors
                while current.neighbors is not None:
                    current = current.neighbors
                current.neighbors = Node(node2)

            if node2.neighbors is None:
                node2.neighbors = Node(node1)
            else:
                current = node2.neighbors
                while current.neighbors is not None:
                    current = current.neighbors
                current.neighbors = Node(node1)

    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def display(self):
        for node in self.nodes:
            print("Node:", node.value)
            print("Neighbors:")
            current = node.neighbors
            while current is not None:
                print(current.value.value)
                current = current.neighbors
            print()


# Example usage
g = Graph()

# Add nodes
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')

# Add edges
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'A')

# Display the graph
g.display()
