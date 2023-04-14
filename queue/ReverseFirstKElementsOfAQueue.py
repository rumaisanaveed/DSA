# Given an integer K and a queue of integers, we need to reverse the order of the first
# K elements of the queue, leaving the other elements in the same relative order.
# The approach is to get the list which consists of the elements in the range k
# and reverse it and concatenate both the list
q = [1,2,3,4]
k = 4
def modifyQueue(q,k):
    lis1 = []
    for i in range(k):
        lis1.append(q[i])

    for i in range(k):
        q.remove(q[0])
    lis1.reverse()
    return lis1 + q
print(modifyQueue(q,k))