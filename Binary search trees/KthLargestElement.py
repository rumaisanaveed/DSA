class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def solve(self, root, k):
        if root is None:
            return
        self.solve(root.right, k)
        self.q.append(root.data)
        self.solve(root.left, k)

    def kthLargest(self, root, k):
        # your code here
        self.q = []
        self.solve(root, k)
        if self.q:
            print(self.q)
            #return self.q[k - 1]
        return -1
node0 = Node(4)
node1 = Node(2)
node2 = Node(9)
node0.left = node1
node0.right = node2
s = Solution()
s.kthLargest(node0,2)
