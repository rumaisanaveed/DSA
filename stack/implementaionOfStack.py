"""How to implement a stack which will support the following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
Push and pop are standard stack operations."""
class Stacks:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def findMiddle(self):
        mid = self.stack[len(self.stack) // 2 : len(self.stack) // 2  + 1]
        return mid[0]

    def deleteMiddle(self):
        m = self.stack[len(self.stack) // 2 : len(self.stack) // 2 + 1]
        self.stack.remove(m[0])
        return self.stack

s = Stacks()
s.push(1)
s.push(2)
s.push(3)
print(s.deleteMiddle())