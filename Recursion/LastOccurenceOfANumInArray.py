def lastIndex(arr,idx,data):
    if idx == len(arr):
        return -1
    liisa = lastIndex(arr,idx+1,data)
    if liisa == -1:
        if arr[idx] == data:
            return idx
        return -1
    return liisa
print(lastIndex([2,3,6,9,8,3,2,3,6,4],0,2))