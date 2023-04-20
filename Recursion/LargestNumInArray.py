def firstIndex(arr,idx,data):
    if idx == len(arr):
        return -1
    fiisa = firstIndex(arr,idx+1,data)
    if arr[idx] == data:
        return idx
    return fiisa