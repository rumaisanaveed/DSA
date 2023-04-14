class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def detectLoop(self,head):
         slow, fast = head, head # n1
         while fast != None and fast.next != None:
             slow = slow.next # slow=n1.next=n2,
             fast = fast.next.next # fast=n1.next.next=n2.next=n3
             if slow == fast:
                return True
         return False
n1 = Node(1)
s = Solution()
n2 = Node(3)
n1.next = n2
n3 = Node(4)
n2.next = n3
print(s.detectLoop(n1))