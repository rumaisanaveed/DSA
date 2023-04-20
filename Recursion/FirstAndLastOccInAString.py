first = -1
last = -1
def findOcurrence(s,idx,element):
    global first
    global last
    if idx == len(s):
        print(first)
        print(last)
        return
    currChar = s[idx]
    if currChar == element:
        if first == -1:
            first = idx
        else:
            last = idx
    findOcurrence(s,idx+1,element)
findOcurrence("abcdaa",0,"a")