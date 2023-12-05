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

    def Approximation(self, nodes):
        pass


    def GreedyBound(self, nodes):
        pass