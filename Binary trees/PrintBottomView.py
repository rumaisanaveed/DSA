class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Function to return a list of nodes visible from the bottom view
    # from left to right in Binary Tree.
    def bottomView(self, root):
        d = {}
        def traverse(root,key,level):
            if root is not None:
                d[key] = [root,level]
                traverse(root.right,key+1,level+1)
                traverse(root.left, key - 1, level + 1)
        traverse(root,0,0)
        res = []
        for key in sorted(d):
            res.append(d[key][0].data)
        return res

node0 = Node(1)
node1 = Node(3)
node2 = Node(2)
node0.left = node1
node0.right = node2
s = Solution()
print(s.bottomView(node0))