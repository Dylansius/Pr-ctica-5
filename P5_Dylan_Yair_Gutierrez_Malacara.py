import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, weight):
        self.edges.append((from_node, to_node, weight))

def kruskal(graph):
    graph.edges = sorted(graph.edges, key=lambda x: x[2])
    mst = []
    mst_graph = nx.Graph()

    for edge in graph.edges:
        from_node, to_node, weight = edge
        if not _forms_cycle(mst, from_node, to_node):
            mst.append((from_node, to_node, weight))
            mst_graph.add_edge(from_node, to_node, weight=weight)

    return mst, mst_graph

def _forms_cycle(mst, from_node, to_node):
    visited = set()
    stack = [(from_node, None)]

    while stack:
        current, parent = stack.pop()
        visited.add(current)
        for node1, node2, _ in mst:
            if current == node1 and node2 != parent:
                if node2 in visited:
                    return True
                stack.append((node2, current))
            elif current == node2 and node1 != parent:
                if node1 in visited:
                    return True
                stack.append((node1, current))
    
    return False

def main():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 1)
    graph.add_edge("B", "D", 7)
    graph.add_edge("C", "D", 3)
    graph.add_edge("C", "E", 5)
    graph.add_edge("D", "E", 6)

    print("Minimum Spanning Tree (Kruskal's Algorithm):")
    mst, mst_graph = kruskal(graph)

    for edge in mst:
        print(f"Add edge: {edge[0]} - {edge[1]} (Cost: {edge[2]})")

    # Visualización gráfica del MST
    pos = nx.spring_layout(mst_graph)
    labels = nx.get_edge_attributes(mst_graph, 'weight')
    nx.draw(mst_graph, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=8)
    nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=labels)
    plt.title("Minimum Spanning Tree (Kruskal's Algorithm)")
    plt.show()

if __name__ == "__main__":
    main()

