import networkx as nx
import matplotlib.pyplot as plt
#instancia
G=nx.Graph()
#diccionario grafo
grafo={"a":["b","c","d","e"]}

for vertice,aristas in grafo.items():
    G.add_node("%s"%vertice)
    for arista in aristas:
        G.add_node(arista)
        G.add_edge((vertice),(arista),weight=1)
        print("%s se conecta con %s"%(vertice,arista))
nx.draw(G,with_labels=True)
plt.show
