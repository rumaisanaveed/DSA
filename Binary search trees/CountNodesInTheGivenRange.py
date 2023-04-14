class Solution:
    def getCount(self,root,low,high):
        ##Your code here
        def traverse(root):
            if root is None:
                return []
            return traverse(root.left) + [root.data] + traverse(root.right)
        arr = traverse(root)
        countOfNodes = 0
        for i in range(len(arr)):
            if arr[i] >= low and arr[i] <= high:
                countOfNodes += 1
        return countOfNodes
