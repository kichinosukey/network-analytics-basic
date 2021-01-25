import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.DiGraph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_edges_from([("A", "E"), ("A", "F"), ("B", "E"), ("B", "F"), ("C", "E"), ("C", "F"), ("D", "F")])

AS = nx.adjacency_matrix(G)
A = AS.todense()
AT = A.transpose()
M = np.dot(AT, A)
M = M - np.diag(np.diag(M))
MB = np.dot(A, AT)
MB = MB - np.diag(np.diag(MB))

print("sparse adjacency matrix:")
print(AS)
print("dense adjacency matrix:")
print(A)
print("co-citation adhacency matrix:")
print(M)
print("bibliographic coupling")
print(MB)