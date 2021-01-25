import networkx as nx
import matplotlib.pyplot as plt 

G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_edges_from([("A", "B"), ("B", "C"), ("B", "D"), ("C", "D"), ("A", "E"), ("C", "E"), ("C", "F")])

plt.subplot(131)
nx.draw_random(G, node_size=400, node_color="red", with_labels=True, font_weight='bold')

plt.subplot(132)
nx.draw_circular(G, node_size=400, node_color="red", with_labels=True, font_weight='bold')

plt.subplot(133)
nx.draw_spring(G, node_size=400, node_color="red", with_labels=True, font_weight='bold')

plt.show()