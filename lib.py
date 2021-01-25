import networkx as nx

def plot_graph(G, how=False):
    if how=='circular':
        draw = nx.draw_circular
    else:
        draw = nx.draw
    draw(G, node_size=400, node_color='red', with_labels=True, font_weight='bold')

def generate_nodes(start, end):
    return list(map(chr, range(ord(start), ord(end)+1)))