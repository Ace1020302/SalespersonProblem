#
#   File:       Algorithms.py
#   Project:    Traveling Salesperson
#   Date:       12.07.23
#   Group:      Algo-Holics (Phillip, Jason, Travis, Noah, Aaron)
#   Purpose:    Class to contain our algorithms
#
from collections import deque
import math
from itertools import permutations
import time
import multiprocessing
from main import readNodes
import networkx as nx

class Algorithms:
    #Naive Brute Force Algo
    def Naive(self, graph, nodes):
        print(self.permute_iterative(nodes, 0, 10, graph, 1000000))
        print('Naive Brute Force', file=open('Results.txt', 'a'))
        print(self.permute_iterative(nodes, 0, 10, graph, 1000000), file=open('Results.txt', 'a'))  # 10 nodes hit
        pass

    # Calculates the path of each individual node between another node
    def calculate_path_cost(self, arr, graph):
        sum = 0
        for i in range(1, len(arr)):
            first_point = arr[i - 1][2]
            second_point = arr[i][2]
            sum += graph[first_point][second_point]
        return sum

    # Every permutation of the possible nodes
    def permute_iterative(self, arr, l, r, graph, dist):
        stack = []  # stack to hold the list of nodes and the first and final index
        stack.append((list(arr), l, r)) #Holds every possible permutations

        source = arr[0]  # Keeping track of what our "source" node is
        start = time.time()
        while stack:
            arr, l, r = stack.pop() #Pops off the latest permutation of the path
            origDist = 0  # Reset original distance

            if l == r:
                if source != arr[0]:
                    source = arr[0]
                    origDist = math.dist([0, 0, 0], arr[0])  # Calculating the distance from the origin to our first point
                newDist = origDist + self.calculate_path_cost(arr, graph)
                if dist > newDist:
                    dist = newDist
            else:
                for i in range(l, r):
                    arr[l], arr[i] = arr[i], arr[l] #Swaps two nodes in the path
                    stack.append((list(arr), l + 1, r)) #Adds that new permutation to the stack
                    arr[l], arr[i] = arr[i], arr[l] #Swaps back
        finalToOrigin = math.dist(arr[r], [0, 0, 0]) #Distance from the last node back to origin
        return time.time() - start, dist + finalToOrigin #Returns the time and the final distance

    #Multiprocessed Permutations
    def permute_optimized(self, head):
        nodes = set(readNodes('tsp_14.txt'))
        nodes.remove(head)
        remainingNodes = nodes
        shortestDist = 10000000000
        dist = None  # Distance at the end of the loop

        for tail in permutations(remainingNodes, 6):  # Tracks for every permutation of the remaining nodes
            if head in tail:  # Ensures no self-edges included
                continue
            distTrack = math.dist([0, 0, 0], head) #Distance from origin to our cutoff head node
            for i in range(1, len(tail) - 1):  # Calculating the distances between each node in the new list
                if i == 1:
                    dist = distTrack + math.dist(head, tail[i])
                    distTrack = dist
                else:
                    dist = distTrack + math.dist(tail[i - 1], tail[i])
                    distTrack = dist
            if math.dist(tail[-1], [0, 0, 0]) + dist < shortestDist:  # If our final distance is shorter than a previous calculated distance, replace it
                shortestDist = math.dist(tail[-1], [0,0,0]) + dist
        return shortestDist

    #Optimized Brute Force Algo
    def optimizer(self, nodes):
        start = time.time()
        with multiprocessing.Pool() as pool:
            all_paths = pool.map(self.permute_optimized, nodes)  # Allocates processes to every processor core in PC, returns a list of all shortest paths
        print(f'Shortest Distance: {min(all_paths)}, Time: {time.time() - start}')
        print('Optimal Brute', file=open('Results.txt', 'a'))
        print(f'Shortest Distance: {min(all_paths)}, Time: {time.time() - start}', file=open('Results.txt', 'a'))  # Takes the shortest of the shortest paths

    # MST and standard pre-order walk approach without any external library
    # prints the cost of the approximated path
    # Returns a Hamiltonian cycle (list) of edges that are apart of the approximation
    # TODO: Go through and find any logical errors in algorithm
    def Older_Approximation(self, edgeGraph, nodes, start):
        # These nodes are actually node objects!
        shortestPath = []

        # Create MST of G using Prims
        print("test")
        mst_walk = self.MST_Prim(edgeGraph, nodes, start, len(nodes))

        print(mst_walk)

        preorder_walk = list(set(mst_walk))
        print("test")
        print(preorder_walk)

        return shortestPath

    # Christofides approximation approach using networkx
    # prints the cost of the approximated path
    # Returns a Hamiltonian cycle (list) of edges that are apart of the approximation
    def N_Approximation(self, networkxGraph: nx.Graph):
        # These nodes are actually node objects!
        shortestPath = []

        nv = networkxGraph.nodes

        # gets the mst
        mst: nx.Graph = nx.minimum_spanning_tree(networkxGraph)

        # Gets the nodes with an odd-degree of edges (1 edge, 3 edges, 5 edges, etc.)
        oddDegreeNodes = [i for i in mst.nodes if mst.degree(i) % 2]

        # Gets the minimum weight perfect matching of the nodes with an odd degree of edges
        matching = nx.min_weight_matching(networkxGraph.subgraph(oddDegreeNodes))

        # Stores matching in a MultiGraph
        matchingGraph:nx.MultiGraph = nx.MultiGraph()

        # Add (into the matching MultiGraph) the nodes from the network
        matchingGraph.add_nodes_from(nv)

        # Merge the nodes that have edges in the mst and the matching
        matchingGraph.add_edges_from(mst.edges())
        matchingGraph.add_edges_from(matching)

        # Source node is the node the circuit starts and loops back to. For this case, we leave it at 'd'
        # Realistically, we could set this as the first node of the network graph
        sourceNode = "d"

        # Initial tour to establish the eulerian circuit
        initTour = nx.eulerian_circuit(matchingGraph, source=sourceNode)

        # This will hold the edges that are a part of the hamilationian cycle
        newTour = []

        # Gets rid of repeating j's in the initial eulerian circuit
        for (i, j) in initTour:
            if j not in newTour:
                newTour.append(j)

        # tour_edges = [(initTour[i-1], initTour[i]) for i in ]
        u = 0
        v = 0
        print(f'NewTour: {newTour}')
        print('Approximation', file=open('Results.txt', 'a'))
        print(f'NewTour: {newTour}', file=open('Results.txt', 'a'))
        sum = 0
        for i in range(1, len(newTour)):
            u = newTour[i - 1]
            v = newTour[i]
            sum += networkxGraph.get_edge_data(u, v)["weight"]

        # Total Distance: 64952.93 from Harrison | 64938.95920682345 from our approx
        # We average in a range of 4,000 margin of error depending on the source node
        print(f'Sum: {sum}')
        print(f'Sum: {sum}', file=open('Results.txt', 'a'))
        return shortestPath

    # MST and Min-Weight-Matching approach without any external library
    # prints the cost of the approximated path
    # Returns a Hamiltonian cycle (list) of edges that are apart of the approximation
    # TODO: Go through and find any logical errors in algorithm
    def Old_Approximation(self, edgeGraph, nodes, start):
        # These nodes are actually node objects!
        shortestPath = []

        mst = self.MST_Prim(edgeGraph, nodes, start, len(nodes))

        oddDegreeNodes = []
        for node in mst:
            # print(f"Node - {node.key:<5} | # of Children - {len(node.children):<5} |  Children {node.getChildrenKeys()}")
            if len(node.children) % 2 != 0:
                oddDegreeNodes.append(node)

        mstEdges = []
        for i in range(len(nodes)):
            for child in nodes[i].children:
                edge = edgeGraph[i][child.key]
                mstEdges.append(edge)

        print("MST GRAPH")


        for edge in mstEdges:
            print(f"edge from {edge.nodeA.key} to {edge.nodeB.key}")

        # After this runs, mstEdges should be the merged version of our MST and the min. weight matching graphs
        print("MIN WEIGHT GRAPH")
        self.minimum_weight_matching(mstEdges, edgeGraph, oddDegreeNodes)

        # Eulerian tour
        ep = self.find_eulerian_tour(mstEdges, edgeGraph, nodes)



        return shortestPath

    # https://github.com/Retsediv/ChristofidesAlgorithm/blob/master/christofides.py
    # Derived from the repo above
    # For nodes with odd degree edges, this will find edges between them such that those edges have the minimum cost
    # TODO: Go through and find any logical errors in algorithm
    def minimum_weight_matching(self, MST, G, odd_vert):
        import random
        random.shuffle(odd_vert)

        # While there are still unpaired odd-degree nodes...
        while odd_vert:
            # v is a random odd-degree node
            v = odd_vert.pop().key
            # The length to the nearest OTHER odd-degree node (u) is not yet found
            # inf = infinity
            length = float("inf")

            # Other variable declarations with sentinels

            # u is the key of a node in the graph
            # u will be an odd-degree node that is not v
            u = 1  # Meaningless here -> this will be a node key

            # closest is index of a node in odd_vert array
            # closest will be the odd-degree node that IS closest to v
            closest = 0

            # Giving this an initial value so it's in an expanded scope
            edgeToAppend = G[0][0]

            # For every other unpaired odd-degree node, u from odd_vert

            for node in odd_vert:
                u = node.key

                # Ensure that v is not u and get the edge distances between them (from complete graph)
                if v != u and G[v][u].distance < length:
                    # length is the DISTANCE
                    length = G[v][u].distance
                    # closest is the NODE
                    closest = u
                    edgeToAppend = G[v][u]


            # add the edges that connect them to the MST
            if(edgeToAppend.nodeA is edgeToAppend.nodeB):
                pass
            else:
                print(f"edge from {edgeToAppend.nodeA.key} to {edgeToAppend.nodeB.key}")
                MST.append(edgeToAppend)

            # prune the node from odd_vert since it was paired with v

            # G[0][closest] is an edge such that nodeA = node with key of 0 and nodeB = node with key of closest
            # for node in odd_vert:
            #     print(f"{node.key}", end=', ')
            # print()
            nodeToRemove = edgeToAppend.nodeB
            if len(odd_vert) > 0:
                odd_vert.remove(nodeToRemove)

    # Finds and returns the edges that are apart of the eulerian tour of the provided Graph MatchedMSTree
    # This is not working nor properly finished
    # TODO: Go through and find any logical errors in algorithm
    def find_eulerian_tour(self, MatchedMSTree, G, nodes):

        print("=" * 100)
        for edge in MatchedMSTree:
            print(f"Edge From {edge.nodeA.key} to {edge.nodeB.key}")

        # find neighbours
        # Node, List of Nodes
        neighbours = {}

        for edge in MatchedMSTree:
            nodeA = edge.nodeA
            nodeB = edge.nodeB

            # Skip if same edge self neighbours
            if(nodeA == nodeB):
                continue

            # Initialize it if it hasn't been already
            if nodeA not in neighbours.keys():
                neighbours[nodeA] = []
            if nodeB not in neighbours.keys():
                neighbours[nodeB] = []

            # If there is an edge connecting to points, we want both points to be in each other's neighbors
            if(nodeB not in neighbours[nodeA]):
                neighbours[nodeA].append(nodeB)

            if(nodeA not in neighbours[nodeB]):
                neighbours[nodeB].append(nodeA)
        # End of for loop

        visitedNodes = []
        currentNode = nodes[0]
        visitedNodes.append(currentNode)
        # Pick a neighbor and see if the edge can safely be removed and if it is not in visitedNodes
        #  - if not move to next neighbour until out of neighbours (should be termination?)
        #  - if so, travel the edge from the graph and then set the current node to the node at end of edge traveled.

        notFinished = True
        while(notFinished):
            neighs = neighbours[currentNode]

            for i in range(len(neighs)):
                # gets the current neighbor node
                currentNeigh = neighs[i]

                # if the index is the same as the length, then it no longer has any nodes to connect to. We are finished
                if i == len(neighs):
                    notFinished = False

                # if the neighbor has been visited before, don't bother connecting to it
                if currentNeigh in visitedNodes:
                    continue # move on to next neighbor

                # If the edge can safely be removed, then travel and restart the whole for loop from that new node
                if self.CanBeRemoved(MatchedMSTree, G[currentNode][currentNeigh]):
                    currentNode = currentNeigh
                    visitedNodes.append(currentNode)
                    break

        # Connect the last currentNode to the start node (it should be a neighbor) to make the cycle

        print("Neighbours: ")
        for nodePar in neighbours.keys():
            listOfStuff = []
            for node in neighbours[nodePar]:
                listOfStuff.append(node.key)
            print(f"{nodePar.key:<3} | {listOfStuff}")

    # Remove edge at coordinate (v1, v2) from the provided graph
    def remove_edge_from_matchedMST(self, MatchedMST, v1, v2):

        for i, edge in enumerate(MatchedMST):
            # print(type(edge))
            if (edge.nodeA.key == v2 and edge.nodeB.key == v1) or (edge.nodeA.key == v1 and edge.nodeB.key == v2):
                MatchedMST.remove(edge)

        return MatchedMST

    # Deprecated Code for the approximation. This involved the pre-order walk
    # DEPRECATED!
    # TODO: Continue research on checking if there is a faster way to implement multiprocessing, this implementation is slower than naive somehow
    def tmp(self, edgeGraph, mst, node_dict, shortestPath, start, nodes):
        node_dict = {node.key: node for node in nodes}

        origin_key = start.key
        origin_node = node_dict[origin_key]
        queue = deque()
        self.preorder_walk(origin_node, queue)
        print("MST")
        for i in range(len(mst)):
            print(mst[i].key, end=', ')
        print()
        print('=' * 50)
        print("PREORDER")
        for i in range(len(queue)):
            print(queue[i].key, end=', ')
        last_node = queue.popleft()
        last_node.children.append(origin_node)
        origin_node.parent = last_node
        weight = 0
        for i in range(len(mst) - 1):
            nodeA, nodeB = mst[i], mst[i + 1]
            weight += edgeGraph[nodeA.key][nodeB.key].distance
        if not shortestPath or weight < shortestPath[-1]:
            shortestPath = [node for node in mst]
        print()
        print('=' * 50)
        print("SHORTEST PATH")
        for i in range(len(shortestPath)):
            print(shortestPath[i].key, end=', ')
        return shortestPath

    # Goes through a given queue of a set of nodes and creates the pre-order walk
    # TODO: Continue research on checking if there is a faster way to implement multiprocessing, this implementation is slower than naive somehow
    def preorder_walk(self, node, queue):
        # shortestPath.append(node.key)
        queue.append(node)
        for child in node.children:
            self.preorder_walk(child, queue)

    # Prim's algorithm implemented such that it is compatible with underlying data structures of project
    # TODO: Go through and find any logical errors in algorithm
    def MST_Prim(self, edgeGraph, nodes, startNode, n):
        # mst arr
        mst = [startNode]
        untouchedNodes = nodes.copy()

        # remove for hamiltonian cycle
        untouchedNodes.remove(startNode)

        for i in range(n):
            if len(untouchedNodes) == 1:
                mst += untouchedNodes  # adds last node to mst
                minEdge = self.findMinEdge(self.getEdgesFromGraph(edgeGraph, untouchedNodes[0], n, []), [])
                nodeA = minEdge.nodeB
                nodeB = minEdge.nodeA

                # This is establishes parentage
                nodeB.parent = nodeA
                nodeA.children.append(nodeB)
                untouchedNodes.remove(untouchedNodes[0])
                break

            # Finds min edge from the frontier
            minEdge = None
            for node in mst:
                edgesOnNode = self.getEdgesFromGraph(edgeGraph, node, n, mst)
                minEdgeOfNode = self.findMinEdge(edgesOnNode, mst)
                if (minEdge is None) or (minEdgeOfNode.distance < minEdge.distance):
                    minEdge = minEdgeOfNode

            nodeA = minEdge.nodeA
            nodeB = minEdge.nodeB

            # This is establishes parentage
            nodeB.parent = nodeA
            nodeA.children.append(nodeB)

            if nodeB in untouchedNodes:
                untouchedNodes.remove(nodeB)
                mst.append(nodeB)

        return mst

    # Finds the minimum edge from a list of edges
    def findMinEdge(self, edges, exclusionList):
        # Find minimum cost edge
        minEdge = edges[0]

        # Finding the min cost edge
        for i in range(1, len(edges)):

            # if edge at index i is less than the current minimum edge then the min edge should be replaced

            if edges[i].distance < minEdge.distance and (edges[i].nodeB not in exclusionList):
                minEdge = edges[i]

        return minEdge

    # Returns all edges stemming from given node -- Except for self-edge (when edge distance == 0)
    def getEdgesFromGraph(self, edgeGraph, node, n, exclusionList):
        # arr of nodes that have an edge to the given node
        arr = []

        # Returns all edges stemming from given node -- Except for self-edge (when edge distance == 0)
        for v in range(n):
            edge = edgeGraph[node.key][v]

            # edge distance != 0 avoids self edge
            if (edge.distance != 0 and (edge.nodeB not in exclusionList)):
                # print("Appended the Edge")
                arr.append(edge)
            else:
                pass
                # print("Did not append")
        return arr