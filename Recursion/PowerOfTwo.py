def powerOfTwo(x):
    if x > 0:
        if x == 0:
            return 1
        return 2 * powerOfTwo(x - 1)

print(powerOfTwo(2))