# This is where we will do the algorithms

class Algorithms:
    def Naive(self, graph, nodes): #Need source, visited paramters
        shortest_path = [] #This is going to be returned
        #current_dist, min_dist = 0

        arr = [nodes[0], nodes[1], nodes[2]]
        print(self.calculate_path_cost(arr, graph))
        #Setup tree structures?
        #Source node goes to every other node, then move to the next (i.e., a to b, a to c, ... then b to c)
        #Cycle till we get the shortest path, or timeout

        #if(current_dist < min_dist):
        #    min_dist = current_dist
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

    def OptimialNaive(self, nodes):
        pass

    def Approximation(self, nodes):
        pass


    def GreedyBound(self, nodes):
        pass