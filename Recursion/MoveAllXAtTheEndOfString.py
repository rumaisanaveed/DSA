def moveX(s,idx,count,newString):
    if idx == len(s) - 1:
        for i in range(count):
            newString += 'x'
        print(newString)
        return
    currChar = s[idx]
    if currChar == 'x':
        count += 1
        moveX(s,idx+1,count,newString)
    else:
        newString += currChar
        moveX(s,idx+1,count,newString)
moveX("xabcdxbx",0,0,"")