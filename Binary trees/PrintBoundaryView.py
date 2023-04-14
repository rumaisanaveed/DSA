class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
        # Code here
        def leftView(self,root,ans):
            if root == None:
                return
            curr = root.left
            while curr is not None:
                ans.append(curr.data)
                curr = curr.left
            ans.pop()

        def leaf(self, root, ans):
            if root == None:
                return
            self.leaf(root.left, ans)

            if root.left == None and root.right == None:
                ans.append(root.data)
            self.leaf(root.right, ans)

        def rightView(self,root,ans):
            if root == None:
                return
            temp = []
            curr = root.right
            while curr is not None:
                temp.append(curr.data)
                curr = curr.right
            if len(temp) != 0:
                 temp.pop()
            temp.reverse()
            return temp

        def printBoundaryView(self, root):
            # Code here
            ans = []
            if root == None:
                return []
            if root.left == None and root.right == None:
                return [root.data]
            ans.append(root.data)
            self.leftView(root,ans)
            self.leaf(root,ans)
            t = self.rightView(root,ans)

            return ans + t


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
print(s.printBoundaryView(node0))