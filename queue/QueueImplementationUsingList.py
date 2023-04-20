import random
class QueueAsList:
    def __init__(self,M,N):
        self.queue = []
        self.M = M
        self.N = N

    def enqueue(self):
        for i in range(N):
            num = random.randint(0,9)
            self.queue.append(num)

    def deque(self):
        for i in range(N):
            a = self.queue[0]
            self.queue.remove(a)

    def displayQueue(self):
        if self.queue == []:
            print([])
        else:
           for i in self.queue:
              print(i,end = " ")
        print()

N = int(input("Enter an integer:"))
M = int(input("Enter an integer:"))
q = QueueAsList(M,N)
for i in range(M):
    q.enqueue()
    print("After adding N elements, the queue is:")
    q.displayQueue()
    print("After removing N elements, the queue is:")
    q.deque()
    q.displayQueue()