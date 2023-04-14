from collections import deque
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    def diagonal(self,root):
        #:param root: root of the given tree.
        #return: print out the diagonal traversal,  no need to print new line
        #code here
        q = deque()
        q.append(root)
        ans = []
        while len(q) > 0:
            curr = q.popleft()
            while curr is not None:
                ans.append(curr.data)
                if curr.left is not None:
                    q.append(curr.left)
                curr = curr.right
        for i in ans:
            print(i,end = " ")
node0 = Node(8)
node1 = Node(3)
node2 = Node(10)
node3 = Node(1)
node4 = Node(6)
node5 = Node(14)
node6 = Node(4)
node7 = Node(7)
node8 = Node(13)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.right = node5
node4.left = node6
node4.right = node7
node5.left = node8
s = Solution()
s.diagonal(node0)
