class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
node0 = TreeNode(10)
node1 = TreeNode(20)
node2 = TreeNode(30)
node3 = TreeNode(40)
node4 = TreeNode(60)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))
length = tree_height(node0)
lst = [None] * length

def printLeftView(root,lst,level):
    if root is None:
        return
    if lst[level] == None:
        lst[level] = root.key
    printLeftView(root.left,lst,level+1)
    printLeftView(root.right,lst,level+1)
    return lst

def main(node0):
    l = printLeftView(node0,lst,0)
    print(l)
    for i in l:
        print(i.key,end=" ")
main(node0)