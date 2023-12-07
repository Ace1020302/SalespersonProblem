# This is where we will do the algorithms
import networkx as nx


class Algorithms:
    def N_Approximation(self, networkxGraph: nx.Graph):
        # These nodes are actually node objects!
        shortestPath = []

        nv = networkxGraph.nodes
        print(networkxGraph)

        # Returns a graph
        mst: nx.Graph = nx.minimum_spanning_tree(networkxGraph)

        print(mst)

        # Gets the nodes with an odd-degree of edges (1 edge, 3 edges, 5 edges, etc.)
        oddDegreeNodes = [i for i in mst.nodes if mst.degree(i) % 2]

        matching = nx.min_weight_matching(networkxGraph.subgraph(oddDegreeNodes))

        matchingGraph:nx.MultiGraph = nx.MultiGraph()

        matchingGraph.add_nodes_from(nv)

        matchingGraph.add_edges_from(mst.edges())
        matchingGraph.add_edges_from(matching)

        # print(matchingGraph)
        initTour = nx.eulerian_circuit(matchingGraph, source='a')
        newTour = []

        # Gets rid of repeating j's in the initial tour
        for (i, j) in initTour:
            if j not in newTour:
                newTour.append(j)

        print(newTour)

        return shortestPath
