class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        # Create two stacks for p and q
        stack_p, stack_q = [p], [q]

        while stack_p and stack_q:
            # Pop the last nodes from the stacks
            node_p, node_q = stack_p.pop(), stack_q.pop()

            # Both nodes are None, continue
            if node_p is None and node_q is None:
                continue

            # One of the nodes is None or their values are different
            if node_p is None or node_q is None or node_p.val != node_q.val:
                return False

            # Add the left and right subtrees to the stacks
            stack_p.append(node_p.right)
            stack_p.append(node_p.left)
            stack_q.append(node_q.right)
            stack_q.append(node_q.left)

        # If both stacks are empty, p and q are the same
        return not stack_p and not stack_q

node0 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(1)
node0.left = node1
node0.right = node2
node3 = TreeNode(1)
node4 = TreeNode(2)
node5 = TreeNode(2)
node3.left = node4
node3.left = node4
s = Solution()
print(s.isSameTree(node0,node3))
