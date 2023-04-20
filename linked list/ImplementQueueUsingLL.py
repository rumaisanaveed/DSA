class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueAsLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def dequeue(self):
        if self.head is None:
            return None
        else:
            a = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return a.data

    def displayQueue(self):
        a = self.head
        while a is not None:
            print(a.data, end=" ")
            a = a.next
        print()

q = QueueAsLL()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("After adding the numbers 1,2,3 into the queue:")
q.displayQueue()
q.dequeue()
print("After removing all the numbers from the queue:")
q.displayQueue()