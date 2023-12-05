# This is where we will do the algorithms

class Algorithms:
    def Naive(self, graph, nodes): #Need source, visited paramters
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

    def Approximation(self, graph, nodes, start):
        shortestPath = []

        # Create MST of G using Prims
        print(self.MST_Prim(graph, nodes, start))

        #

        return shortestPath



    def MST_Prim(self, graph, nodes, start):
        mst = []
        # Add first vertex into tree
        mst.append(start)

        edges = self.getEdgesFromGraph(start, nodes, graph)

        current_node = start

        while len(mst) < len(nodes):
            minEdge = self.findMinEdge(graph, current_node, edges)
            mst.append(minEdge)
            for edge in self.getEdgesFromGraph(minEdge, nodes, graph):
                if(edge not in edges):
                    edges.append(edge)
            edges.remove(minEdge)

        return mst


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