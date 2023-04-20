def countPaths(i,j,n,m):
    if i == n or j == m:
        return 0
    if i == n - 1 and j == m - 1:
        return 1
    # move downwards
    downPaths = countPaths(i+1,j,n,m)

    # move right
    rightPaths = countPaths(i,j+1,n,m)

    return downPaths + rightPaths

totalPaths = countPaths(0,0,3,3)
print(totalPaths)