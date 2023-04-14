class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def compute(self,head):
        curr = head
        prev = None
        while curr is not None:
            if curr.next is not None and curr.next.data > curr.data:
                if prev is not None:
                    prev.next = curr.next
                else:
                    head = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        curr = head
        while (curr is not None):
            print(curr.data,end = " ")
            curr = curr.next

n1 = Node(10)
s = Solution()
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
n5 = Node(50)
n4.next = n5
n6 = Node(60)
s.compute(n1)
