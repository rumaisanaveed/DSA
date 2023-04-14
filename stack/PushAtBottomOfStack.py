#Push the given element at the bottom of stack
from queue import LifoQueue
def pushAtBottom(data, stack):
    if (stack.empty()):
        stack.put(data)
        return
    top = stack.get()
    pushAtBottom(data,stack)
    stack.put(top)
stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
pushAtBottom(4, stack)
while (not(stack.empty())):
    print(stack.get())