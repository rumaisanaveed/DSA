class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def inorderSucc(n):
    if n.right is not None:
        return minValue(n.right)
    p = n.parent
    while p is not None:
        if n != p.right:
            break
        n = p
        p = p.parent

    return p

def minValue(root):
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr

def insert(node,data):
    if node is None:
        return TreeNode(data)
    else:
        if data <= node.val:
            temp = insert(node.left,data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node

root = None
root = insert(root, 20)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10)
root = insert(root, 14)
temp = root.left.right.right
succ = inorderSucc(temp)
if succ is not None:
    print(f"The inorder successor of {temp.val} is {succ.val}.")
else:
    print("\nInorder Successor doesn't exist")