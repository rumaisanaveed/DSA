class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    # code here
    q = []
    ans = []
    q.append(root)
    while q != []:
        root = q.pop(0)
        ans.append(root.data)
        if root.right is not None:
            q.append(root.right)
        if root.left is not None:
            q.append(root.left)
    ans.reverse()
    return ans

n0 = Node(10)
n1 = Node(20)
n0.left = n1
n2 = Node(30)
n0.right = n2
n3 = Node(40)
n1.left = n3
n4 = Node(60)
n1.right = n4
print(reverseLevelOrder(n0))