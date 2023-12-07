import math
import webbrowser
from tabulate import tabulate
import networkx as nx
import numpy
from pyvis.network import Network
import matplotlib.pyplot as plt

import Algorithms

# Text boxes
# Phillip:  This is where we type to one another during live share
# Levi:
# Travis:
# Noah:
# Jason:
import AlgorithmsTMP
from Edge import Edge
from Node import Node


def visualSeparator():
    print('===' * 100)
    print('===' * 100)
    print('===' * 100)


def readNodes(fileName, skipFirstLine=True):
    arr = []

    file = open(fileName)

    # Skips first line if it's not a point
    if (skipFirstLine):
        file.readline()

    label = 0
    for line in file:
        a, b = line.split()
        a = int(a)
        b = int(b)
        arr.append((a, b, label))
        label += 1

    file.close()
    return arr


def readNewNodes(fileName, skipFirstLine=True):
    arr = []

    file = open(fileName)

    # Skips first line if it's not a point
    if skipFirstLine:
        file.readline()

    key = 0
    for line in file:
        a, b = line.split()
        a = int(a)
        b = int(b)
        node = Node(None, None, None)
        node.coords = (a, b)
        node.key = key  # Index needed to access element in our graph
        arr.append(node)
        key += 1

    file.close()
    return arr


def getDist(a, b):
    # Message to show getDist step in compute_graph
    # print(f"getDist :: a = {a} | b = {b}")
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
            if (adj_mat[i][j] != 0):
                continue
            # if (i == j):
            #   continue
            # Calculate value once for each node.
            distance = getDist(nodes[i], nodes[j])
            adj_mat[i][j] = distance
            adj_mat[j][i] = distance
            # Message to clarify distance calculation per-step after getDist
            # print(f"compute_graph :: Distance between Node {i} {nodes[i]} and Node {j} {nodes[j]} = {adj_mat[i][j]}")
            # print('--' * 100)
    return adj_mat


def printGraph(graph, labels):
    if len(graph[0]) > len(labels):
        print("Can't print table, not enough labels")
        return
    for i in range(len(labels)):
        graph[i].insert(0, labels[i])
    labels.insert(0, '')
    print(tabulate(graph, headers=labels, tablefmt="fancy_grid", floatfmt=".3f", numalign="center"))
    labels.remove('')
    for i in range(len(labels)):
        graph[i].remove(labels[i])


def compute_edge_graph(nodes):
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
            if (adj_mat[i][j] != 0):
                continue
            # Calculate value once for each node.
            distance = getDist(nodes[i].coords, nodes[j].coords)
            edge = Edge(nodes[i], nodes[j], distance)
            adj_mat[i][j] = edge
            mirroredEdge = Edge(nodes[j], nodes[i], distance)
            adj_mat[j][i] = mirroredEdge
            # Message to clarify distance calculation per-step after getDist
            # print(
            # f"compute_graph :: Distance between Node {i} {nodes[i]} and Node {j} {nodes[j]} = {adj_mat[i][j]}")
            # print('--' * 100)
    return adj_mat


def draw_plot():
    plt.show()


def run():
    nodes = readNodes("tsp_14.txt")
    new_nodes = readNewNodes("tsp_14.txt")
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

    # Testing Purposes Only
    g = nx.Graph()
    graph = (compute_graph(nodes))
    edge_graph = compute_edge_graph(new_nodes)

    # Add Nodes to network
    for i in range(len(nodes)):
        g.add_node(labels[i])
    # Separators
    visualSeparator()

    for i in range(len(graph)):
        for j in range(len(graph)):
            if (i == j):
                continue
            # print(f"Edge Weight to be added: From {labels[i]} to {labels[j]} --- {graph[i][j]}, {type(graph[i][j])}")
            g.add_edge(labels[i], labels[j], weight=graph[i][j])

    printGraph(graph, labels)

    pos = nx.spring_layout(g, seed=3113794652)

    option = input("0: Quit\n1: Brute\n2: Optimal Brute\n3: Approximation\nInput: ")
    option = int(option)
    while option != 0:
        # print(option)
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            algo = AlgorithmsTMP.Algorithms()
            tmpVar = algo.N_Approximation(g)
        option = input("0: Quit\n1: Brute\n2: Optimal Brute\n3: Approximation\nInput: ")
        option = int(option)


    print("goodbye")
    # nx.draw(g, pos=pos, with_labels=True)

    # algo.optimizer(nodes)
    # plt.savefig("filename.png")


def find_shortest_path(g, graph, labels):
    shortPath = nx.dijkstra_path(g, 'g', 'd')
    totalDistance = 0
    for i in range(len(shortPath)):
        if i == 0:
            continue
        # label idx of to find equivalent adj_mat position
        x = labels.index(shortPath[i - 1])
        y = labels.index(shortPath[i])

        # Get the node with that label and look up the distance between the two nodes (adj_mat)
        print(f"Distance from {shortPath[i - 1]} to {shortPath[i]}: {graph[x][y]}")
        totalDistance += graph[x][y]

        # print
        print(totalDistance)


def __init__():
    run()


#
if __name__ == "__main__":
    run()
    # draw_plot()
