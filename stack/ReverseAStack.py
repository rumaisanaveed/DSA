from queue import LifoQueue

'''First solution'''
s = LifoQueue()
s.put(1)
s.put(2)
s.put(3)
newStack = LifoQueue()
while (not(s.empty())):
    newStack.put(s.get())
while (not(newStack.empty())):
    print(newStack.get())

'''Second solution'''
def pushAtBottom(data, stack):
    if (stack.empty()):
        stack.put(data)
        return
    top = stack.get()
    pushAtBottom(data,stack)
    stack.put(top)
def reverse(stack):
    if (stack.empty()):
        return
    top = stack.get()
    reverse(stack)
    pushAtBottom(top,stack)
stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
reverse(stack)
while (not(stack.empty())):
    print(stack.get())
