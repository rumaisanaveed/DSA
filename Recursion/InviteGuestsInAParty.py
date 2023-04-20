'''Find the number of ways in which you can invite n people to your party single or in pairs'''

def callGuests(n):
    if n <= 1:
        return 1
    ways1 = callGuests(n-1)
    ways2 = (n-1) * callGuests(n-2)
    return ways1 + ways2
print(callGuests(3))