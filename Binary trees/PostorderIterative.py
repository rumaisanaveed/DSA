class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def postOrderIterative(root):
    if root is None:
        return
    stack = []
    while (True):
        while (root):
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()
        if (root.right is not None and
                peek(stack) == root.right):
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            print(root.data,end = " ")
            root = None

        if (len(stack) <= 0):
            break

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Post Order traversal of binary tree is")
postOrderIterative(root)