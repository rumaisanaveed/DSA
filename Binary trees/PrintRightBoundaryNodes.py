class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def printBoundaryRightNodes(root):
    curr = root
    while curr is not None:
        print(curr.data,end=" ")
        curr = curr.right

n0 = Node(10)
n1 = Node(20)
n0.left = n1
n2 = Node(30)
n0.right = n2
n3 = Node(40)
n1.left = n3
n4 = Node(60)
n1.right = n4
printBoundaryRightNodes(n0)