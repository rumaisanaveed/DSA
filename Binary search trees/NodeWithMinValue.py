class TreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def minValue(root):
    if root is None:
        return -1

    while root.left is not None:
        root = root.left
    return root.data

node0 = TreeNode(20)
node1 = TreeNode(8)
node2 = TreeNode(22)
node3 = TreeNode(4)
node4 = TreeNode(12)
node5 = TreeNode(10)
node6 = TreeNode(14)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node4.left = node5
node4.right = node6
min = minValue(node0)
print(f"The minimum value in ths bst is {min}.")