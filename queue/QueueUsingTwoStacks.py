class QueueY:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self,data):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(data)

        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return not self.s1

    def printQueue(self):
        for i in self.s1:
            print(i)

q = QueueY()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print(q.peek())
q.pop()
print(q.peek())