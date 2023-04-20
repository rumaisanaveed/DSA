class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def reverseLinkedList(self,head):
        if head == None or head.next == None:
            return head
        newHead = self.reverseLinkedList(head.next)
        headNext = head.next
        headNext.next = head
        head.next = None
        return newHead

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
s.reverseLinkedList(n1)