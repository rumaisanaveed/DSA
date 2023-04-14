class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
prev = None

def isbst(node):
    global prev
    if node != None:
        if (not(isbst(node.left))):
            return False
        if prev != None and node.data <= prev.data:
            return False
        prev = node
        return isbst(node.right)
    return True
node0 = Node(20)
node1 = Node(10)
node2 = Node(40)
node3 = Node(5)
node4 = Node(15)
node5 = Node(30)
node6 = Node(50)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
print(isbst(node0))