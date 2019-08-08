import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

G = nx.MultiDiGraph()
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 7.0), ('c', 'd', 15.0), \
        ('a', 'd', 5.0), ('b', 'd', 3.0), ('a', 'b', 7.0), ('c', 'a', 15.0)]
G.add_weighted_edges_from(elist)
pos = nx.layout.spring_layout(G)

node_sizes = [10 + 10 * i for i in range(len(G))]
M = G.number_of_edges()
edge_colors = range(3, M + 3)
edge_alphas = [(5 + i) / (M + 4) for i in range(M)]

nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='magenta')
edges = nx.draw_networkx_edges(G, pos, node_size=node_sizes, arrowstyle='-|>',
                               arrowsize=10, edge_color=edge_colors,
                               edge_cmap=plt.cm.Greys, width=2)
for i in range(M):
    edges[i].set_alpha(edge_alphas[i])

pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Greys)
pc.set_array(edge_colors)
plt.colorbar(pc)

ax = plt.gca()
ax.set_axis_off()
plt.show()
