import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from lib import plot_graph, generate_nodes

G = nx.Graph()
G.add_nodes_from(generate_nodes('A', 'F'))
G.add_edges_from([
    ("A", "B"), ("B", "C"), ("B", "D"), ("C", "D"), ("A", "E"), ("C", "E"), ("C", "F")
    ])

plt.figure(figsize=(5, 5))
plot_graph(G)

A = nx.adjacency_matrix(G).todense()
AA = A**2 # or np.dot(A, A) or A.dot(A)
AAA = A**3
print(A)
print(AA)
print(AAA)

plt.show()