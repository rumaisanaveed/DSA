# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def reverseList(self,head):
        curr = head
        prev = None
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def removeNthFromEnd(self,head,n):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        a = self.reverseList(head)
        # if node is present at end
        if n == 1:
            a = a.next
            h = self.reverseList(a)
            return h
        # If node is present at the beginning
        elif n == count:
            prev = a
            currNode = a.next
            while currNode.next is not None:
                currNode = currNode.next
                prev = prev.next
            prev.next = None
            h = self.reverseList(a)
            return h
        # This part handles the middle nodes
        else:
             prevNode = a
             currNode = prevNode.next
             for i in range(1, n - 1):
                 currNode = currNode.next
                 prevNode = prevNode.next
             prevNode.next = currNode.next
             currNode.next = None
             h = self.reverseList(a)
             return h
        while h is not None:
            print(h.data,end = " ")
            h = h.next

n1 = Node(1)
s = Solution()
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next = n5
s.removeNthFromEnd(n1,5)