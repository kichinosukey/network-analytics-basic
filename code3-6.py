import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_edges_from([("A", "B"), ("B", "C"), ("B", "D"), ("C", "D"), ("A", "E"), ("C", "E"), ("C", "F")])

print("degree:", G.degree())
print(nx.degree_histogram(G))
print(nx.info(G))
plt.bar(range(5), height=nx.degree_histogram(G))
plt.show()