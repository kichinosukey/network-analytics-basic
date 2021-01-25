import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

from lib import plot_graph

B = nx.Graph()
B.add_nodes_from([1, 2, 3, 4], bipartite=0)
B.add_nodes_from(['a', 'b', 'c'], bipartite=1)
B.add_edges_from([
    (1, 'a'), (1, 'b'), (2, 'b'), (2, 'c'), (3, 'c'), (4, 'a')
    ])

plt.subplot(131)
plot_graph(B)

top_nodes = set(n for n, d in B.nodes(data=True) if d['bipartite']==0)
bottom_nodes = set(B) - top_nodes
print("top nodes:", top_nodes)
print("bottom nodes:", bottom_nodes)

GT = bipartite.projected_graph(B, top_nodes)
print("projected graph (top nodes):", GT.edges())

plt.subplot(132)
plot_graph(GT)

GB = bipartite.projected_graph(B, bottom_nodes)
print("projected graph (bottom nodes):", GB.edges())

plt.subplot(133)
plot_graph(GB)

plt.show()