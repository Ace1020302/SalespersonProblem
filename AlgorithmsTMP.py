# This is where we will do the algorithms
import networkx as nx

class Algorithms:
    def N_Approximation(self, networkxGraph:nx.Graph):
        # These nodes are actually node objects!
        shortestPath = []

        nv = networkxGraph.nodes
        print(networkxGraph)

        # Returns a graph
        mst:nx.Graph = nx.minimum_spanning_tree(networkxGraph)

        print(mst)


        oddVertices = []
        verticies = (mst.degree)
        print(verticies)

        for vertex in verticies:
            if vertex[1] % 2 != 0:
                oddVertices.append(vertex[0])
        print(oddVertices)
        # Remove the odd vertices from the mst graph here then run the min weight on a graph with those removed vertices?
        # Add odd vertices edges to one another to mst?

        # This is a set of edges such that these edges do not have common vertices
        minWeightMatch = nx.min_weight_matching(mst)
        print(minWeightMatch)

        removeTheseFromOther = []
        # Remove the pairs that are not part of the Odd Vertices
        for pair in minWeightMatch:
            if(pair[0] not in oddVertices) and (pair[1] not in oddVertices):
                removeTheseFromOther.append(pair)

        for pair in removeTheseFromOther:
            minWeightMatch.remove(pair)

        print(minWeightMatch)
        return shortestPath