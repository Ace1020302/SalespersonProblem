import math
import webbrowser
import networkx as nx
import numpy
from pyvis.network import Network
import matplotlib.pyplot as plt


def readNodes(fileName, skipFirstLine=True):
    arr = []

    file = open(fileName)

    # Skips first line if it's not a point
    if(skipFirstLine):
        file.readline()

    for line in file:
        a, b = line.split()
        a = int(a)
        b = int(b)
        arr.append((a, b))

    file.close()
    return arr


def getDist(a, b):
    # Message to show getDist step in compute_graph
    print(f"getDist :: a = {a} | b = {b}")
    # grab one of the y's and one of the x's
    return math.dist(a, b)


def compute_graph(nodes):
    # Store the graph with the distances. This is really an adjacency matrix (2D array)
    # Set up adjacency matrix dimensions, square matrix len(nodes) by len(nodes)
    nodeCount = len(nodes)
    # Initialize with 0 for sentinel
    adj_mat = [[0 for i in range(nodeCount)] for j in range(nodeCount)]
    # method 2 1st approach
    # Store nodeCount instead of recalculating len(nodes) every loop

    for i in range(nodeCount):
        for j in range(nodeCount):
            # Don't calculate repeated distances
            if(adj_mat[i][j] != 0):
                continue
            # Calculate value once for each node.
            distance = getDist(nodes[i], nodes[j])
            adj_mat[i][j] = distance
            adj_mat[j][i] = distance
            # Message to clarify distance calculation per-step after getDist
            print(f"compute_graph :: Distance between Node {i} {nodes[i]} and Node {j} {nodes[j]} = {adj_mat[i][j]}")
            print('--'*100)
    return adj_mat


nodes = readNodes("tsp_14.txt")
# "tsp_14.txt"

graph = (compute_graph(nodes))
print('==='*100)

for i in range(len(graph)):
    for j in range(len(graph)):
        print("{0}".format(graph[i][j]), end='\t')
    print()
    print()



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



