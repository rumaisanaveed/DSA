#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        return (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right))
n0 = TreeNode(1)
s = Solution()
print(s.inorderTraversal(n0))