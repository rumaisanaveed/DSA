keypad = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def printComb(s,idx,comb):
    if idx == len(s):
        print(comb)
        return
    currChar = s[idx]
    mapping = keypad[ord(currChar) - ord('2')]
    for i in range(len(mapping)):
        printComb(s,idx+1,comb+mapping[i])
printComb("23",0,"")