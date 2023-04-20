def sumOfSeries(n):
    if n == 1:
        return 1
    return n + sumOfSeries(n - 1)
print(sumOfSeries(4))