map = [False] * 26
def removeDuplicates(s,idx,newString):
    global map
    if idx == len(s):
        print(newString)
        return
    currChar = s[idx]
    if map[ord(currChar) - ord('a')] == True:
        removeDuplicates(s,idx+1,newString)
    else:
       newString += currChar
       map[ord(currChar) - ord('a')] = True
       removeDuplicates(s,idx+1,newString)
removeDuplicates("geeksforgeek",0,"")