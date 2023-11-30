import webbrowser
import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt




net = Network()

# net.addNode("A")
# net.addNode("B")
#
#
# net.addEdge("A", "B", 10)
# net.addEdge("B", "A", 5)



g = nx.Graph()
pos = nx.spring_layout(g, seed=3113794652)

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(3, 3)
g.add_edge(6, 4)


nx.draw_networkx(g, with_labels=True)


net.from_nx(g)


# plt.show()
net.show("nx.html", notebook=False)


webbrowser.open('http://localhost:63342/TravelingSalesperson/nx.html')

# plt.savefig("filename.png")

