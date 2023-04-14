class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMedian(root):
    # code here
    # return the median
    def inorderTraversal(root):
        if root is None:
            return []
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
    arr = inorderTraversal(root)
    if len(arr) % 2 == 0:
        midIndex = len(arr) // 2
        median = (arr[midIndex - 1] + arr[midIndex]) / 2
        return median
    else:
        midIndex = len(arr) // 2
        median = arr[midIndex]
        return median

node0 = TreeNode(6)
node1 = TreeNode(3)
node2 = TreeNode(8)
node3 = TreeNode(1)
node4 = TreeNode(4)
node5 = TreeNode(7)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
print(findMedian(node0))
