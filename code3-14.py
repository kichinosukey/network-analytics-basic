import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from lib import plot_graph, generate_nodes

G = nx.DiGraph()
G.add_nodes_from(generate_nodes("A", "F"))
G.add_edges_from([
    ("A", "C"), ("C", "B"), ("B", "F"), ("F", "D"), 
    ("F", "E"), ("D", "E"), ("E", "C"), ("D", "A")
])

A = nx.adjacency_matrix(G).todense()
print("A: diag = ", np.diag(A))
print(A)

AA = A**2
print("A * A: diag = ", np.diag(AA))
print(AA)

AAA = A**3
print("A * A * A: diag = ", np.diag(AAA))
print(AAA)

AAAA = A**4
print("A * A * A * A: diag = ", np.diag(AAAA))
print(AAAA)

plt.figure()

plot_graph(G)
plt.show()