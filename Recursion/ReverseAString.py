def reverseString(idx,string):
    if idx == 0:
        print(string[idx])
        return
    print(string[idx],end="")
    reverseString(idx-1,string)
reverseString(len("for")-1,"for")