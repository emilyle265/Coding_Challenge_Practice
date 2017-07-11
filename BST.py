class Node:
    def __init__(self, val):
        self.val = val
        self.rightChild = None
        self.leftChild = None

    def getChildren(self):
        children = []
        if self.leftChild:
            children.append(self.leftChild)
        if self.rightChild:
            children.append(self.rightChild)

class Node:
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
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if val < currentNode.val:
            self.findNode(currentNode.leftChild, val)
        elif val > currentNode.val:
            self.findNode(currentNode.rightChild, val)
        elif val == currentNode.val:
            return True

        return False

    def getRoot(self):
        return self.root

    def setRoot(self, val):
        self.root = val

    def height(self):
        return actual_height(self.root)

    def actual_height(self, currentNode):
        if currentNode is None:
            return 0 
        else:
            return 1 + max(actual_height(currentNode.leftChild), actual_height(currentNode.rightChild))
