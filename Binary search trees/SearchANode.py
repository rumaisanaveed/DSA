class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        elif val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right,val)
        elif val < root.val:
            return self.searchBST(root.left,val)
