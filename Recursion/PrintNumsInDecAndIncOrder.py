def pdi(n):
    if n == 0:
        return
    print(n)
    pdi(n-1)
    print(n)
pdi(5)