import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiGraph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_edges_from([("A", "B"), ("B", "C"), ("B", "D"), ("C", "D"), ("A", "E"), ("C", "E"), ("C", "F"), ("C", "F"), ("F", "F")])

print("degree:", G.degree())
nx.draw(G, node_size=400, node_color='red', with_labels=True, font_weight='bold')
print(nx.info(G))
plt.show()