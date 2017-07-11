class Node:
    def __init__(self, val):
        self.val = val
        self.rightChild = None
        self.leftChild = None

    def getChildren(self):
        children = []
        if self.rightChild:
            children.append(self.rightChild)
        if self.leftChild:
            children.append(self.leftChild)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val <= currentNode.val:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif val >= currentNode.val:
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if val < currentNode.val:
            self.findNode(currentNode.leftChild, val)
        elif val > currentNode.val:
            self.findNode(currentNode.rightChild, val)
        elif currentNode.val == val:
            return True

        return False

    def getRootVal(self):
        return self.root

    def setRootVal(self, val):
        self.root = val

    def is_valid(self):
        self.ok(self.root, None, None)

    def ok(self, currentNode, lt, gt):
        if currentNode. 



