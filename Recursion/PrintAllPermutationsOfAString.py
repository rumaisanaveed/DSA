def printPerm(str,permutation):
    if len(str) == 0:
        print(permutation)
        return
    for i in range(len(str)):
        currChar = str[i]
        newStr = str[0:i] + str[i+1:]
        printPerm(newStr,permutation+currChar)
printPerm("absg","")