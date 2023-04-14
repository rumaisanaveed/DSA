def push1(a, x):
    a.insert(0, x)

def push2(a, x):
    a.insert(len(a), x)

def pop1(a):
    if len(a):
        return a.pop(0)
    return -1

def pop2(a):
    if len(a):
        return a.pop(len(a) - 1)
    return -1

push1([],2)