class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head is None:
           node = Node(data)
           self.head = node
        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.data

    def peek(self):
        a = self.head
        return a.data

    def displayStack(self):
        a = self.head
        while a is not None:
            print(a.data,end = " ")
            a = a.next
        print()

s = Stack()
print("After adding the numbers 1 to 5 in the stack:")
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.displayStack()
print("After removing the last number from the stack:")
s.pop()
s.displayStack()
print("After getting the top:")
print(s.peek())