class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def sortedArrToBst(self,arr):
        if len(arr) == 0:
            return None
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        # For left subtree
        root.left = self.sortedArrToBst(arr[:mid])
        # For right subtree
        root.right = self.sortedArrToBst(arr[mid+1:])
        return root

s = Solution()
s.sortedArrToBst([1,2,3])