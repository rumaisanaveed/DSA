class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def isPalindrome(self, head):
        if head is None:
            return True
        mid = self.middle(head)
        last = self.reverse(mid)
        curr = head
        while last != None:
            if last.val != curr.val:
                return False
            last = last.next
            curr = curr.next
        return True

    def middle(self, h):
        slow = h
        fast = h
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, m):
        curr = m
        prev = None
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev


s = Solution()
n1 = Node(1)
n2 = Node(2)
n1.next = n2
print(s.isPalindrome(n1))