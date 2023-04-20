def printArrInReverseOrder(arr,idx):
    if idx == len(arr):
        return
    printArrInReverseOrder(arr,idx+1)
    print(arr[idx])
printArrInReverseOrder([1,2,3,4,5],0)