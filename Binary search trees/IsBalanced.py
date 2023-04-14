class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self, root):

        # add code here
        if root is None:
            return True
        return abs(self.findHeight(root.left) - (self.findHeight(root.right))) < 2 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def findHeight(self, root):
        if root is None:
            return -1
        return 1 + max(self.findHeight(root.left), self.findHeight(root.right))

node0 = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(60)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
s = Solution()
print(s.isBalanced(node0))