# This is where we will do the algorithms
import copy


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

    def MST_Prim(self, edgeGraph, nodes, startNode, n):
        # mst arr
        mst = []
        tmpUnchecked = nodes.copy()
        s = startNode
        for i in range(n):
            if len(tmpUnchecked) == 1:
                mst += tmpUnchecked
                break

            minEdge = self.findMinEdge(self.getEdgesFromGraph(edgeGraph, s, n, mst))
            nextNode = minEdge.nodeB
            mst.append(s)
            # print(tmpUnchecked)
            if(s in tmpUnchecked):
                print(s.key, " in tmpUnchecked. Will be removed.")
            else:
                print(s.key, " in not tmpUnchecked. Will not be removed. Major Tom to ground control")
            tmpUnchecked.remove(s)
            s = nextNode
            print(s.key, " is new node")
            print("=" * 50)


        return mst

    def findMinEdge(self, edges):
        # Find minimum cost edge
        minEdge = edges[0]

        # Finding the min cost edge
        for i in range(1, len(edges)):

            # if edge at index i is less than the current minimum edge then the min edge should be replaced
            if edges[i].distance < minEdge.distance:
                minEdge = edges[i]

        return minEdge

    # Returns all edges stemming from given node -- Except for self-edge (when edge distance == 0)
    def getEdgesFromGraph(self, edgeGraph, node, n, exclusionList):
        # arr of nodes that have an edge to the given node
        arr = []

        # Returns all edges stemming from given node -- Except for self-edge (when edge distance == 0)
        for v in range(n):
            checkingEdge = edgeGraph[node.key][v]
            print(checkingEdge.nodeA.key, checkingEdge.nodeB.key)
            # edge distance != 0
            if (checkingEdge.distance != 0 and (checkingEdge.nodeB not in exclusionList)):
                print("Appended the Edge")
                arr.append(checkingEdge)
            else:
                print("Did not append")
        return arr

    def GreedyBound(self, nodes):
        pass
