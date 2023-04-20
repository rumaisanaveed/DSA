def firstIndex(arr,idx,data):
    if idx == len(arr):
        return -1
    if arr[idx] == data:
        return idx
    fiisa = firstIndex(arr, idx + 1, data)
    return fiisa

print(firstIndex([1,2,3,4,5,2,4,3],0,2))