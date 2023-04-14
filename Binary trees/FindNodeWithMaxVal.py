class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def findMax(self,root):
        if root is None:
            return 1
        largestLeft = self.findMax(root.left)
        largestRight = self.findMax(root.right)
        maximum = max(root.data,largestLeft,largestRight)
        return maximum

node0 = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(6)
node6 = Node(7)
node7 = Node(8)
node8 = Node(9)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
node4.left = node7
node4.right = node8
s = Solution()
print(s.findMax(node0))