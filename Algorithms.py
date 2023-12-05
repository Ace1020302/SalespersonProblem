# This is where we will do the algorithms

class Algorithms:
    def Naive(self, graph, nodes): #Need source, visited paramters
        shortest_path = []
        arr = [nodes[0], nodes[1], nodes[2]]
        print(self.permute(nodes, 0, 14, graph))

        return shortest_path
        pass

    #Calculates the path of each individual node between another node
    def calculate_path_cost(self, arr, graph):
        sum = 0
        for i in range(1, len(arr)):
            first_point = arr[i - 1][2]
            second_point = arr[i][2]
            sum += graph[first_point][second_point]
        return sum

    #TODO: Add functionality to track when source node changes and increment a counter to keep track
    #TODO: Fix error where currentDist is called every time and the shortest distance is incorrect
    def permute(self, arr, l, r, graph):
        import time
        currentDist = 1000000
        list = []
        counter = 0

        if l == r:
            newDist = self.calculate_path_cost(arr, graph)
            print('Distance: ', newDist)
            print(newDist)
            if currentDist > newDist:
                currentDist = newDist
                print('New Shortest Distance: ', currentDist)
            time.sleep(4)
        else:
            for i in range(l,r):
                arr[l], arr[i] = arr[i], arr[l]
                self.permute(arr, l + 1, r, graph)
                arr[l], arr[i] = arr[i], arr[l]


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