def printArray(arr,idx):
    if idx == len(arr):
        return
    print(arr[idx])
    printArray(arr,idx+1)
printArray([6,4,5,7,8,9],0)