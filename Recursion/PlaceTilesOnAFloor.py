'''Place tiles of size 1xm in a floor of size nxm'''

def placeTiles(n,m):
    if n == m:
        return 2
    if n < m:
        return 1
    vertPlacements = placeTiles(n-m,m)

    horPlacements = placeTiles(n-1,m)

    return vertPlacements + horPlacements

print(placeTiles(5,4))