from Edge import Edge
from Node import Node


class Network:
    def __init__(self):
        self.nodes = []
        self.edges = []

    # Add Node Methods
    def addNode(self, label: str):
        node = Node(label)
        try:
            self.checkNodeConflict(node)
            self.nodes.append(node)
        except:
            print("Conflicting Nodes > not adding node " + label)


    # Get Node Method
    def getNode(self, label: str):
        for node in self.nodes:
            if node.label == label:
                return node

    # Add Edge Methods
    def addEdge(self, labelA: str, labelB: str, cost):
        edge = Edge(self.getNode(labelA), self.getNode(labelB), cost)
        try:
            self.checkEdgeConflict(edge)
            self.edges.append(edge)
        except:
            print("Conflicting Edges > not adding edge Node: " + labelA + " Node: " + labelB)


    # Conflict methods
    def checkEdgeConflict(self, edge: Edge):
        for inEdge in self.edges:
            if (inEdge.nodeA == edge.nodeA) and (inEdge.nodeB == edge.nodeB):
                raise KeyError

    def checkNodeConflict(self, node: Node):
        for inNode in self.nodes:
            if inNode.label == node.label:
                raise KeyError

    def printNetwork(self):
        sepAmt = 75
        print("="*sepAmt)
        print("Nodes")
        print("-"*sepAmt)
        for node in self.nodes:
            print(f"Node: {node.label}")
        if (len(self.nodes) == 0):
            print("No Nodes")
        print("="*sepAmt)

        print("")

        print("="*sepAmt)
        print("Edges")
        print("-"*sepAmt)
        for edge in self.edges:
            print(f"Edge: from Node {edge.nodeA.label} to {edge.nodeB.label} with cost of {edge.cost}")

        if (len(self.edges) == 0):
            print("No Edges")
        print("="*sepAmt)

    def __str__(self):
        self.printNetwork()
        return ""