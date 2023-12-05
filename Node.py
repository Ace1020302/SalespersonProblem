class Node:
    def __init__(self, key, parent, coords, label=""):
        self.label = label
        self.key = key
        self.parent = parent
        self.coords = coords # tuple (x, y)
