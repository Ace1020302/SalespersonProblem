import math
import webbrowser
import networkx as nx
import numpy
from pyvis.network import Network
import matplotlib.pyplot as plt

# Text boxes
# Phillip:  sure give me a sec
# Levi:
# Travis:
# Noah:
# Jason:

def visualSeparator():
    print('===' * 100)
    print('===' * 100)
    print('===' * 100)

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
            # if (i == j):
            #   continue
            # Calculate value once for each node.
            distance = getDist(nodes[i], nodes[j])
            adj_mat[i][j] = distance
            adj_mat[j][i] = distance
            # Message to clarify distance calculation per-step after getDist
            print(f"compute_graph :: Distance between Node {i} {nodes[i]} and Node {j} {nodes[j]} = {adj_mat[i][j]}")
            print('--'*100)
    return adj_mat



nodes = readNodes("tsp_14.txt")
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']


# Testing Purposes Only
# For pyvis
net = Network()

# For nx
g = nx.Graph()
# pos = nx.spring_layout()
graph = (compute_graph(nodes))
print('==='*100)
print('==='*100)
print('==='*100)


# Add Nodes to network
for i in range(len(nodes)):
    g.add_node(labels[i])


# Separators
visualSeparator()

# Add Our Weights
# for i in range(len(graph)):
#     for j in range(len(graph)):
#         print(f"Edge Weight to be added: {graph[i][j]}, {type(graph[i][j])}")
#         g.add_edge(graph[i], graph[j], weight=graph[i][j])

for i in range(len(graph)):
    for j in range(len(graph)):

        if(i == j):
            continue
        print(f"Edge Weight to be added: From {labels[i]} to {labels[j]} --- {graph[i][j]}, {type(graph[i][j])}")
        g.add_edge(labels[i], labels[j], weight=graph[i][j])

visualSeparator()

for i in range(len(graph)):
    for j in range(len(graph)):
        print("{0}".format(graph[i][j]), end='\t')
    print()
    print()

visualSeparator()

# Compute the shortest path in g from node a to node b
shortPath = nx.dijkstra_path(g, 'g', 'd')

totalDistance = 0
for i in range(len(shortPath)):
    if i == 0:
        continue
    # label idx of to find equivalent adj_mat position
    x = labels.index(shortPath[i-1])
    y = labels.index(shortPath[i])

    # Get the node with that label and look up the distance between the two nodes (adj_mat)
    print(f"Distance from {shortPath[i-1]} to {shortPath[i]}: {graph[x][y]}")
    totalDistance += graph[x][y]

    # print
    print(totalDistance)

# net.addNode("A")
# net.addNode("B")
#
#
# net.addEdge("A", "B", 10)
# net.addEdge("B", "A", 5)


#
# g = nx.Graph()
pos = nx.spring_layout(g, seed=3113794652)
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
nx.draw(g, pos=pos, with_labels=True)

# nx.draw_networkx_edge_labels(g, pos, edge_labels=nx.get_edge_attributes(g,'weight'))
#
#
# net.from_nx(g)


plt.show()
# net.show("nx.html", notebook=False)
#
#
# webbrowser.open('http://localhost:63342/TravelingSalesperson/nx.html')

# plt.savefig("filename.png")



