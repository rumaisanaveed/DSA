def printNumsInReverseOrder(n):
    if n == 0:
        return
    print(n)
    printNumsInReverseOrder(n-1)
printNumsInReverseOrder(5)