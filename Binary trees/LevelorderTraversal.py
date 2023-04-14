class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    q = []
    q.append(root)
    while q != []:
        curr = q.pop(0)
        print(curr.data,end=" ")
        if curr.left != None:
            q.append(curr.left)
        if curr.right != None:
            q.append(curr.right)

n0 = Node(1)
n1 = Node(2)
n0.left = n1
n2 = Node(3)
n0.right = n2
n3 = Node(2)
n1.left = n3
n4 = Node(1)
n1.right = n4
n5 = Node(6)
n4.left = n5
n6 = Node(7)
n4.right = n6
levelOrderTraversal(n0)
