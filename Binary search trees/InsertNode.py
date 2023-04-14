class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right,val)
        return root

node0 = TreeNode(4)
node1 = TreeNode(2)
node2 = TreeNode(7)
node3 = TreeNode(1)
node4 = TreeNode(3)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
s = Solution()
s.insertIntoBST(node0,5)