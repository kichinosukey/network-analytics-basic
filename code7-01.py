import networkx as nx
import matplotlib.pyplot as plt

from lib import plot_graph

er = nx.erdos_renyi_graph(100, 0.1)
plt.subplot(241)
nx.draw(er, node_size=10, node_color='red')
print(nx.info(er))
plt.subplot(245)
plt.plot(nx.degree_histogram(er))

ba = nx.barabasi_albert_graph(100, 3)
plt.subplot(242)
nx.draw(ba, node_size=10, node_color='red')
print(nx.info(ba))
plt.subplot(246)
plt.plot(nx.degree_histogram(ba))

K_100 = nx.complete_graph(100)
plt.subplot(243)
nx.draw(K_100, node_size=10, node_color='red')
print(nx.info(K_100))
plt.subplot(247)
plt.plot(nx.degree_histogram(K_100))

karate = nx.karate_club_graph()
plt.subplot(244)
nx.draw(karate, node_size=10, node_color='red')
print(nx.info(karate))
plt.subplot(248)
plt.plot(nx.degree_histogram(karate))

plt.show()