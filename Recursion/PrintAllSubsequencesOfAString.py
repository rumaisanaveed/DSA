def subsequences(s,idx,newString):
    if idx == len(s):
        print(newString)
        return
    currChar = s[idx]
    subsequences(s,idx+1,newString+currChar)
    subsequences(s,idx+1,newString)
subsequences("abc",0,"")