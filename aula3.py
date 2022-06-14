from os import remove
import networkx as nx
import matplotlib.pyplot as plt

def shift (pos, x_shift, y_shift):
    return {n:(x + x_shift, y + y_shift) for n, (x, y) in pos.items()}

G = nx.MultiGraph()
G.add_nodes_from(range (1, 21))

students = ('Amadeu L.', 'Anna C.', 'Augusto R.', 'Fillipe M.', 'Gabriel C.', 'Gabriel M.', 'Guilherme A.', 'Gustavo M.', 'Igor G.', 'Jonathan F.', 'Lucas B.', 'Lucas I.','Marcos R.', 'Matheus G.', 'Müller R.', 'Pedro L.', 'Rafael E.', 'Ricardo S.', 'Vitor L.', 'Wilker T.')
relations = ('Axé', 'Bossa Nova', 'Eletrônica', 'Funk', 'Gospel', 'Indie', 'MPB', 'Música Clássica', 'Pagode', 'Pop', 'Rock', 'Sertanejo', 'Soundtracks')
cs_course = (2, 9, 12, 13, 15, 20)
se_course = (1, 3, 4, 5, 6, 7, 8, 10, 11, 14, 16, 17, 18, 19)
#edgelabel_persist = ((11,19), (6, 17), (6, 9), (9, 20), (16, 14), (10, 7), (20, 4), (17, 12), (7, 8), (4, 20), (2, 5), (4, 1), (1, 13), (1, 3), (8, 15))


G.add_edges_from([(1, 8), (1, 15), (8, 15)], color="#ED4E0E", r=relations[relations.index("Axé")])
G.add_edges_from([(11, 19), (11, 18), (18, 19)], color="#0B7EE6", r=relations[relations.index("Bossa Nova")])
G.add_edges_from([(10, 14), (10, 16), (14, 16)], color="#FCCA06", r=relations[relations.index("Eletrônica")])
G.add_edges_from([(17, 11), (17, 6), (11, 6)], color="#6EC9DF", r=relations[relations.index("Gospel")])
G.add_edges_from([(7, 8), (7, 12), (8, 12)], color="#129340", r=relations[relations.index("Indie")])
G.add_edges_from([(19, 17), (19,12), (12, 17)], color="#441293", r=relations[relations.index("MPB")])
G.add_edges_from([(1, 2), (1, 13), (2, 13)], color="#931228", r=relations[relations.index("Música Clássica")])
G.add_edges_from([(3, 4), (3, 15), (4, 15)], color="#C10000", r=relations[relations.index("Pagode")])
G.add_edges_from([(2 ,5), (2, 13), (5, 13)], color="#B200C1", r=relations[relations.index("Pop")])
G.add_edges_from([(5, 7), (5,10), (7, 10)], color="#720000", r=relations[relations.index("Rock")])
G.add_edges_from([(4, 14), (4, 20), (14, 20)], color="#41F000", r=relations[relations.index("Sertanejo")])
G.add_edges_from([(6, 9), (6, 16), (9, 16)], color="#696969", r=relations[relations.index("Soundtracks")])
G.add_edges_from([(9, 10), (9, 20), (10, 20)], color="#E66EFF", r=relations[relations.index("Funk")])

pos = nx.kamada_kawai_layout(G)
pos_shift = shift(pos, 0, 0.1)
colors = nx.get_edge_attributes(G, 'color').values()

label_options = {
    "font_size":8.5,
    "font_weight":'bold',
    "font_family":'arial',
}

labels = {}
for i in range(20):
    labels[i+1] = students[i]
nx.set_node_attributes(G, labels, "nome")
test = nx.get_node_attributes(G, "nome")
print(test)

nx.draw_networkx_nodes(G, pos, nodelist=tuple(set(G.nodes()) & set(cs_course)), node_color="#F07030", node_size=250)
nx.draw_networkx_nodes(G, pos, nodelist=tuple(set(G.nodes()) & set(se_course)), node_color="#59A3DD", node_size=250)
nx.draw_networkx_edges(G, pos, edge_color=colors, width=1.8)
nx.draw_networkx_labels(G, pos=pos_shift, labels= test, **label_options)
#nx.draw_networkx_edge_labels(G, pos)

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
