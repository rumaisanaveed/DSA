def printNumsInDecreasingOrder(n):
    if n == 0:
        return
    print(n)
    printNumsInDecreasingOrder(n-1)
printNumsInDecreasingOrder(100)