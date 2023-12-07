#
#   File:       Edge.py
#   Project:    Traveling Salesperson
#   Date:       12.07.23
#   Group:      Algo-Holics (Phillip, Jason, Travis, Noah, Aaron)
#   Purpose:    Models our edges
#
class Edge:
    def __init__(self, nodeA, nodeB, distance=0):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.distance = distance

    def setDistance(self, distance):
        self.distance = distance

    def setNodes(self, nodeA, nodeB):
        self.nodeA = nodeA
        self.nodeB = nodeB