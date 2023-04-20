def isSorted(arr,idx):
    if idx == len(arr) - 1:
        return True
    if arr[idx] < arr[idx+1]:
        return isSorted(arr,idx+1)
    return False
print(isSorted([1,3,3,5],0))