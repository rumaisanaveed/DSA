class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def topView(root):
    d = {}
    def traverse(root,key,level):
        if root is not None:
            if key not in d:
                d[key] = [root,level]

            traverse(root.left,key-1,level+1)
            traverse(root.right,key+1,level+1)
    traverse(root,0,0)
    res = []
    for key in sorted(d):
        res.append(d[key][0].val)
    return res

node0 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(3)
node4 = TreeNode(6)
node5 = TreeNode(4)
node0.left = node1
node0.right = node2
node2.left = node3
node2.right = node4
node3.right = node5
print(topView(node0))