class Node:
    def __init__(self, key, parent=None, coords=(None, None), label=""):
        self.label = label
        self.key = key
        self.parent = parent
        self.coords = coords # tuple (x, y)
        self.children = []
