class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

n0 = TreeNode(3)
s = Solution()
n1 = TreeNode(9)
n0.left = n1
n2 = TreeNode(20)
n0.right = n2
n3 = TreeNode(15)
n2.left = n2
n4 = TreeNode(7)
n2.right = n4
print(s.maxDepth(n0))