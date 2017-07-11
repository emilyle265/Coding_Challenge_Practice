def add(self, val):
    if self.root is None:
        self.root = Node(val)
    else:
        self.addNode(self.root, val)

def addNode(self, currentNode, val):
    if val <= currentNode.val:
        if currentNode.leftChild:
            self.addNode(currentNode.leftChild, val)
        else:
            currentNode.leftChild = Node(val)
    elif val >= currentNode.val:
        if currentNode.rightChild:
            self.addNode(currentNode.rightChild, val)
        else:
            currentNode.rightChild = Node(val)