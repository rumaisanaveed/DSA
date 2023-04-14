class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
     def find(self,root,key):
         if root is None:
             return None
         elif key == root.val:
             return root
         elif key > root.val:
             return self.find(root.right,key)
         elif key < root.val:
             return self.find(root.left,key)

     def update(self,root,newValue,prevVal):
           target = self.find(root,prevVal)
           if target is not None:
              target.val = newValue

node0 = TreeNode(2)
node1 = TreeNode(1)
node2 = TreeNode(3)
node0.left = node1
node0.right = node2
s = Solution()
s.update(node0,1,5)