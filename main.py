import webbrowser
import networkx as nx
import numpy
from pyvis.network import Network
import matplotlib.pyplot as plt


def readNodes(fileName):
    arr = []

    file = open(fileName)
    file.readline()
    for line in file:
        a, b = line.split()
        a = int(a)
        b = int(b)
        arr.append((a, b))

    file.close()
    return arr


def getDist(a, b):
    #grab one of the y's and one of the x's
    return numpy.hypot(a[0], b[1])

def compute_graph(nodes):
    # Store the graph with the distances. This is really an adjacency matrix (2D array)
    adj_mat = [[]]
    for i in nodes:
        for j in nodes:
            adj_mat[i][j] = getDist(i, j)
    return adj_mat


nodes = readNodes("tsp_14.txt")
# "tsp_14.txt"

print(compute_graph(nodes))
# print(nodes)



net = Network()

# net.addNode("A")
# net.addNode("B")
#
#
# net.addEdge("A", "B", 10)
# net.addEdge("B", "A", 5)


#
# g = nx.Graph()
# pos = nx.spring_layout(g, seed=3113794652)
#
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 4)
# g.add_edge(1, 4)
# g.add_edge(1, 5)
# g.add_edge(3, 3)
# g.add_edge(6, 4)
#
#
# nx.draw_networkx(g, with_labels=True)
#
#
# net.from_nx(g)


# plt.show()
# net.show("nx.html", notebook=False)
#
#
# webbrowser.open('http://localhost:63342/TravelingSalesperson/nx.html')

# plt.savefig("filename.png")



