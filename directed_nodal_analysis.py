import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

# 1) get lat long of each sId
# 2) calculate padded bounds
# 3) add nodes
# G=nx.Graph()
# G.add_node(1,pos=(1,1))
# G.add_node(2,pos=(2,2))
# G.add_edge(1,2)
# pos=nx.get_node_attributes(G,'pos')
# pos
# {1: (1, 1), 2: (2, 2)}
# nx.draw(G,pos)

G = nx.MultiDiGraph()
relDict = {('a','b'):'5', \
        ('b','c'):'3', ('c','d'):'15'}
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 7.0), ('c', 'd', 15.0), \
       ('a', 'd', 5.0), ('b', 'd', 3.0), ('a', 'b', 7.0), ('c', 'a', 15.0)]
# elist is a list of tuples of node connections (for each rel. (cell, euT, pm))
# In dict labeling form, tuple[0] for cell, tuple[1] for nb, tuple[2] for pm

G.add_weighted_edges_from(elist)
pos = nx.layout.spring_layout(G)

M = G.number_of_edges()
edge_colors = range(3, M + 3)
edge_alphas = [(5 + i) / (M + 4) for i in range(M)]

nodes = nx.draw_networkx_nodes(G, pos, node_size=300, node_color='magenta', node_shape='2')
edges = nx.draw_networkx_edges(G, pos, node_size=200, arrowstyle='-|>',
                               arrowsize=10, edge_color=edge_colors,
                               edge_cmap=plt.cm.Greys, width=2,
                               labels={node:node for node in G.nodes()})
nx.draw_networkx_edge_labels(G, pos, edge_labels=relDict, font_color='black')
# edge_labels is a dict of tuple keys and pm identical to elist

for i in range(M):
    edges[i].set_alpha(edge_alphas[i])

pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Greys)
pc.set_array(edge_colors)
plt.colorbar(pc)

ax = plt.gca()
ax.set_axis_on()
plt.axis('on')
plt.show()
