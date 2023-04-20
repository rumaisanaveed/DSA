def checkPalindrome(s):
    s1 , s2 = [] , []
    for i in range(len(s)):
        s1.append(s[i])
    for j in range(len(s)-1,-1,-1):
        s2.append(s[j])
    while s1 and s2:
        if s1.pop() != s2.pop():
            return False
    return True
s = input("Enter a word:")
res = checkPalindrome(s)
if res:
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")