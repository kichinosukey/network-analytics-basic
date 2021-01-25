import networkx as nx
import matplotlib.pyplot as plt

from lib import plot_graph

G = nx.DiGraph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_edges_from([("A", "E"), ("A", "F"), ("B", "E"), ("B", "F"), ("C", "E"), ("C", "F"), ("D", "F")])

plt.subplot(121)
plot_graph(G)

GC = nx.MultiGraph()
GC.add_nodes_from(["E", "F"])
GC.add_edges_from([("E", "F"), ("E", "F"), ("E", "F")])

plt.subplot(122)

plot_graph(GC)
plt.show()