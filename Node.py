#
#   File:       Node.py
#   Project:    Traveling Salesperson
#   Date:       12.07.23
#   Group:      Algo-Holics (Phillip, Jason, Travis, Noah, Aaron)
#   Purpose:    Models our nodes
#

class Node:
    def __init__(self, key, parent=None, coords=(None, None), label=""):
        self.label = label
        self.key = key
        self.parent = parent
        self.coords = coords # tuple (x, y)
        self.children = []

    def getChildrenKeys(self) -> []:
        arr = []
        for child in self.children:
            arr.append(child.key)
        return arr
