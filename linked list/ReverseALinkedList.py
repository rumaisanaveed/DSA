class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val # val=5 , val=10 , val=15, val=20
        self.next = next # next=None , next=None , next=None , next=None

class Solution:
    def reverseList(self, head):
        curr = head # n1
        prev = None
        while (curr != None):
            nextNode = curr.next # n2 , n3 , n4 , None
            curr.next = prev
            prev = curr # prev=n1, prev=n2 , prev=n3 , prev=n4
            curr = nextNode # curr=n2 , curr=n3 , curr=n4 , curr=None

        while prev != None: # prev=n4->n3->n2->n1
            print(prev.val,end = " ") # n4.val=20
            prev = prev.next # prev=n4.next=n3

n1 = ListNode(5)
s = Solution() # s.head=n1
n2 = ListNode(10)
n1.next = n2
n3 = ListNode(15)
n2.next = n3
n4 = ListNode(20)
n3.next = n4
s.reverseList(n1)
