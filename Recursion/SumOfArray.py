def sumArray(arr,idx,s):
    if idx == len(arr):
        print(s)
        return
    sumArray(arr,idx+1,s+arr[idx])
sumArray([1,2,3],0,0)