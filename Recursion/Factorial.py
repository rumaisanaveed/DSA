def findFactorial(n):
    if n == 1:
        return 1
    return n * findFactorial(n-1)
print(findFactorial(3))