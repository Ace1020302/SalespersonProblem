# This is where we will do the algorithms
import copy
import sys
from collections import deque

from Edge import Edge
from Node import Node


class Algorithms:
    def Naive(self, graph, nodes):
        # sanity check
        arr1 = [(-193, 8782, 2), (-5168, 2636, 3), (-4521, 1266, 11), (-7005, 2118, 6),
                (-9860, 1311, 13), (-9955, -2923, 5), (-8022, -3864, 4), (-7795, -5000, 10), (-3138, -2512, 0),
                (7775, -8002, 7), (9478, -1973, 9), (6804, -1072, 1), (4244, -1339, 8), (-192, 3337, 12)]
        print(self.permute_iterative(nodes, 0, 10, graph, 1000000))  # 10 nodes hit
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
        import time
        import math

        stack = []  # stack to hold the list of nodes and the first and final index
        stack.append((list(arr), l, r))

        source = arr[0]  # Keeping track of what our "source" node is
        start = time.time()
        while stack:
            arr, l, r = stack.pop()
            origDist = 0  # Reset original distance

            if l == r:
                if source != arr[0]:
                    source = arr[0]
                    origDist = math.dist([0, 0, 0],
                                         arr[0])  # Calculating the distance from the origin to our first point
                    print(f'From Origin: {0, 0} + {arr[0]} = {origDist}')
                newDist = origDist + self.calculate_path_cost(arr, graph)
                print(f'Distance: {newDist}')
                time.sleep(5)
                if dist > newDist:
                    dist = newDist
                    print(f'New Shortest Distance: {dist}')
                print(arr)
            else:
                for i in range(l, r):
                    arr[l], arr[i] = arr[i], arr[l]
                    stack.append((list(arr), l + 1, r))
                    arr[l], arr[i] = arr[i], arr[l]
        finalToOrigin = math.dist(arr[r], [0, 0, 0])
        print(f'Final Node To Origin: {arr[r]} + {[0, 0]} = {finalToOrigin}')
        return time.time() - start, dist + finalToOrigin

    def OptimialNaive(self, nodes):
        pass

    def Approximation(self, edgeGraph, nodes, start):
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

    def N_Approximation(self, edgeGraph, nodes, start):
        # These nodes are actually node objects!
        shortestPath = []



        mst = self.MST_Prim(edgeGraph, nodes, start, len(nodes))


        for node in mst:
            print(f"Node - {node.key:<5} | # of Children - {len(node.children):<5} |  Children {node.getChildrenKeys()}")

        for i in range(len(mst)):
            print(mst[i].key, end=', ')

        return shortestPath

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

    def preorder_walk(self, node, queue):
        # shortestPath.append(node.key)
        queue.append(node)
        for child in node.children:
            self.preorder_walk(child, queue)


    def MST_Prim(self, edgeGraph, nodes, startNode, n):
        # mst arr
        mst = [startNode]
        untouchedNodes = nodes.copy()


        for i in range(n):
            if len(untouchedNodes) == 1:
                mst += untouchedNodes # adds last node to mst
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

        # Node A -> Node B -> Node D -> Node C

        # Node A -> Node B -> Node C -> Node D

        return mst


    def findMinEdge(self, edges, exclusionList=None):
        # Find minimum cost edge
        minEdge = edges[0]

        # Finding the min cost edge
        for i in range(1, len(edges)):

            # if edge at index i is less than the current minimum edge then the min edge should be replaced
            if edges[i].distance < minEdge.distance and (edges[i].nodeB not in exclusionList):
                minEdge = edges[i]

        return minEdge

    # Returns all edges stemming from given node -- Except for self-edge (when edge distance == 0)
    def getEdgesFromGraph(self, edgeGraph, node, n, exclusionList=None):
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

    def GreedyBound(self, nodes):
        pass
