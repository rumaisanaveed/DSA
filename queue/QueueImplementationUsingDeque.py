import random
from collections import deque

class QueueAsDeque:
    def __init__(self,N):
        self.queue = deque()
        self.N = N

    def enqueue(self):
        for i in range(N):
           self.queue.appendleft(random.randint(0,9))

    def deque(self):
        for i in range(N):
           self.queue.popleft()

    def displayQueue(self):
        if self.queue == deque([]):
            print([])
        else:
            for i in self.queue:
                print(i,end = " ")
        print()

N , M = 5 , 1
q = QueueAsDeque(N)
for i in range(M):
    q.enqueue()
    print("After adding the N elements, the queue is:")
    q.displayQueue()
    q.deque()
    print("After removing the N elements, the queue is:")
    q.displayQueue()