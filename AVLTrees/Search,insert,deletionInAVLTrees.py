class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
        self.height = 1

class AVLTree:
    def insertion(self,root,key):
        # perform normal bst insertion
        if root is None:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insertion(root.left,key)
        else:
            root.right = self.insertion(root.right,key)

        # update the height of the root node
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        # Calculate the balanced factor
        balanceF = self.getBalance(root)

        # If the tree is unbalanced then, there are 4 cases
        # right right case
        if balanceF < -1 and key > root.right.val:
            return self.leftRotate(root)
        # left left case
        elif balanceF > 1 and key < root.left.val:
            return self.rightRotate(root)
        # right left case
        elif balanceF < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        # left right case
        elif balanceF > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # None of the above case
        else:
            return root

    def search(self,root,key):
        if root is None:
            return False
        if key == root.val:
            return True
        elif key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def delete(self,root,key):
        if root is None:
            return root
        elif key < root.val:
            root.left = self.delete(root.left,key)
        elif key > root.val:
            root.right = self.delete(root.right,key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,temp.val)
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        elif balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        elif balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        elif balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        else:
            return root

    def getMinValueNode(self, root):
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr

    def getHeight(self,root):
        if root is None:
            return 0
        return root.height

    def getBalance(self,root):
        if root is None:
            return 0
        return (self.getHeight(root.left) - self.getHeight(root.right))

    def leftRotate(self,z):
        y = z.right
        T2 = y.left
        # perform rotation
        y.left = z
        z.right = T2
        # update heights
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))

        return y

    def rightRotate(self,z):
        y = z.left
        T3 = y.right
        # perform rotation
        y.right = z
        z.left = T3
        # update heights
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))

        return y

    def preOrder(self, root):
        if root is None:
            return
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

myTree = AVLTree()
root = None
root = myTree.insertion(root, 10)
root = myTree.insertion(root, 20)
root = myTree.insertion(root, 30)
root = myTree.insertion(root, 40)
root = myTree.insertion(root, 50)
root = myTree.insertion(root, 25)
print("Preorder traversal of the constructed AVL tree after insertion of nodes is:")
myTree.preOrder(root)
print()
print("Search for the node with value 30:")
myTree.search(root,30)
myTree.delete(root,40)
print("After deletion of node with value 40, the preorder traversal is:")
myTree.preOrder(root)