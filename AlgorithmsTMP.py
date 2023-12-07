# This is where we will do the algorithms
import networkx as nx


class Algorithms:
    def N_Approximation(self, networkxGraph: nx.Graph):
        # These nodes are actually node objects!
        shortestPath = []

        nv = networkxGraph.nodes

        # Returns a graph
        mst: nx.Graph = nx.minimum_spanning_tree(networkxGraph)

        #print(mst)

        # Gets the nodes with an odd-degree of edges (1 edge, 3 edges, 5 edges, etc.)
        oddDegreeNodes = [i for i in mst.nodes if mst.degree(i) % 2]

        matching: nx.Graph = nx.min_weight_matching(networkxGraph.subgraph(oddDegreeNodes))

        matchingGraph:nx.MultiGraph = nx.MultiGraph()

        matchingGraph.add_nodes_from(nv)

        matchingGraph.add_edges_from(mst.edges())
        matchingGraph.add_edges_from(matching)

        # print(matchingGraph)
        sourceNode = "d"
        initTour = nx.eulerian_circuit(matchingGraph, source=sourceNode)

        newTour = []

        # Gets rid of repeating j's in the initial tour
        for (i, j) in initTour:
            if j not in newTour:
                newTour.append(j)

        #tour_edges = [(initTour[i-1], initTour[i]) for i in ]
        u = 0
        v = 0
        print(newTour)
        sum = 0
        for i in range(1, len(newTour)):
            u = newTour[i - 1]
            v = newTour[i]
            sum += networkxGraph.get_edge_data(u, v)["weight"]

        # Total Distance: 64952.93 from Harrison | 64938.95920682345 from our approx
        print(sum)
        return shortestPath
