"""Question: Design a Data Structure SpecialStack that supports all the stack operations like
push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return
minimum element from the SpecialStack. All these operations of SpecialStack must be O(1).
To implement SpecialStack, you should only use standard Stack data structure and no other
data structure like arrays, list etc."""
def push(arr, ele):
    # Code here
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    # Code here
    arr.pop()

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    if len(arr) == n:
        return True
    return False

# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    if len(arr) == 0:
        return True
    return False

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    return min(arr)
