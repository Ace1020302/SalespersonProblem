# This is where we will do the algorithms

class Algorithms:
    def Naive(self, graph, nodes):
        #sanity check
        arr1 = [ (-193, 8782, 2), (-5168, 2636, 3), (-4521, 1266, 11), (-7005, 2118, 6),
                 (-9860, 1311, 13), (-9955, -2923, 5), (-8022, -3864, 4), (-7795, -5000, 10), (-3138, -2512, 0),
                 (7775, -8002, 7), (9478, -1973, 9), (6804, -1072, 1), (4244, -1339, 8), (-192, 3337, 12)]
        print(self.permute_iterative(nodes, 0, 10, graph, 1000000)) #10 nodes hit
        pass

    #Calculates the path of each individual node between another node
    def calculate_path_cost(self, arr, graph):
        sum = 0
        for i in range(1, len(arr)):
            first_point = arr[i - 1][2]
            second_point = arr[i][2]
            sum += graph[first_point][second_point]
        return sum

    #Every permutation of the possible nodes
    #https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/#
    def permute_iterative(self, arr, l, r, graph, dist):
        import time
        import math

        stack = [] #stack to hold the list of nodes and the first and final index
        stack.append((list(arr), l, r))

        source = arr[0] #Keeping track of what our "source" node is
        start = time.time()
        while stack:
            arr, l, r = stack.pop()
            origDist = 0 #Reset original distance

            if l == r:
                if source != arr[0]:
                    source = arr[0]
                    origDist = math.dist([0,0,0], arr[0]) #Calculating the distance from the origin to our first point
                    print(f'From Origin: {0, 0} + {arr[0]} = {origDist}')
                newDist = origDist + self.calculate_path_cost(arr, graph)
                print(f'Distance: {newDist}')
                time.sleep(5)
                if dist > newDist: #Checking if we have a new smallest distance and re-initializing
                    dist = newDist
                    print(f'New Shortest Distance: {dist}')
                print(arr)
            else:
                for i in range(l, r): #This whole block swaps around the nodes so that there is one new permutation each run
                    arr[l], arr[i] = arr[i], arr[l]
                    stack.append((list(arr), l + 1, r))
                    arr[l], arr[i] = arr[i], arr[l]
        finalToOrigin = math.dist(arr[r], [0, 0, 0])
        print(f'Final Node To Origin: {arr[r]} + {[0, 0]} = {finalToOrigin}')
        return time.time() - start, dist + finalToOrigin #returns final total distance + the distance from the last node to origin

    def OptimialNaive(self, nodes):
        # https://www.geeksforgeeks.org/parallel-processing-in-python/
        # import multiprocessing
        # import timer
        pass

    def Approximation(self, edge_graph, nodes, start):
        shortestPath = []

        # Create MST of G using Prims
        print("test")
        mst_walk = self.MST_Prim(edge_graph, nodes, start)
        print(mst_walk)

        preorder_walk = list(set(mst_walk))
        print("test")
        print(preorder_walk)

        return shortestPath



    def MST_Prim(self, edge_graph, nodes, start):
        # Set of which nodes (keys) have been indexed. Node[2] = key of node
        mstNodes = []

        # Get the edges connected to the node minus self edges
        edges = self.getEdgesFromGraph(start, nodes, edge_graph)

        # Sets the current node to the start node
        current_node = start

        n = len(nodes)
        for u in n:
            minEdge = self.findMinEdge(edge_graph, current_node, edges)
            mstNodes.append(current_node) # Adds key of the node to the searched list
            for v in n:
               notInSet = True
               # mst[i] = (x, y, key) @ index i
               # mst[i][2] = key at index
               if(nodes[v] in mstNodes):
                   notInSet = False

               if (edge_graph[u][v] > 0) and (notInSet) and (start > edge_graph[u][v]):
                   start = edge_graph[u][v]

            current_node = minEdge # Grabs the node that the current node connects to?
        return mstNodes


    def findMinEdge(self, graph, node, edges):
        # Find minimum cost edge
        minEdge = edges[0]

        # Finding the min cost edge
        for i in range(len(edges)):
            if(graph[node[2]][minEdge[2]] > graph[node[2]][edges[i][2]]):
                minEdge = edges[i]

        return minEdge


    def getEdgesFromGraph(self, node, nodes, graph):
        # arr of nodes that have an edge to the given node
        arr = []
        node_key = node[2]
        for i in range(len(graph[node_key])):
            # Avoid Self Edges
            if(i == node_key):
                continue
            else:
                arr.append(nodes[i])
        return arr


    def GreedyBound(self, nodes):
        pass