from collections import deque
def checkPalindrome(s):
    queue = deque()
    for i in range(len(s)-1,-1,-1):
        queue.appendleft(s[i])
    reverseStr = ""
    while queue:
        reverseStr += queue.pop()
    if reverseStr == s:
        return f"{s} is a palindrome."
    return f"{s} is not a palindrome."
s = input("Enter a word to check if it is palidrome or not:")
print(checkPalindrome(s))