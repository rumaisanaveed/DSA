#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        return ([root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right))
n0 = TreeNode()
s = Solution()
n1 = TreeNode(2)
n0.right = n1
n2 = TreeNode(3)
n1.left = n2
print(s.preorderTraversal(n0))
