
class Edge:
    def __init__(self, nodeA, nodeB, cost=0):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.cost = cost

    def setCost(self, cost):
        self.cost = cost

    def setNodes(self, nodeA, nodeB):
        self.nodeA = nodeA
        self.nodeB = nodeB