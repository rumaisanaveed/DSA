class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def preOrder(root):
    stack = []
    stack.append(root)
    while stack != []:
        currNode = stack.pop()
        print(currNode.data, end =" ")
        if currNode.right is not None:
            stack.append(currNode.right)
        if currNode.left is not None:
            stack.append(currNode.left)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
preOrder(root)