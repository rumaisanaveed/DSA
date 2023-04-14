"""Algorithm
We will create a stack and push all the persons in that stack.
We will compare every 2 persons and if we will find that A knows B
we will discard it and push the other one again in the stack and
the process will be continued till only one person left in the stack.
The person which we will get may be he is the celebrity or not.We will
check it by finding the whole row and column.If the row consists entirely
of zeroes and column contains 1 then,the person is the celebrity otherwise,
he is not."""

class Solution():

    def rowCheck(self,M, stk):
        for r in range(len(M)):
            if M[stk[0]][r] != 0:
                return False
        return True

    def colCheck(self,M, stk):
        for c in range(len(M[0])):
            if stk[0] != c:
                if M[c][stk[0]] != 1:
                    return False
        return True

    def celebrity(self,M,n):
        stk = []
        for i in range(n):
            stk.append(i)

        while (len(stk) > 1):
            A = stk.pop()
            B = stk.pop()
            if M[A][B] == 1:
                stk.append(B)
            else:
                stk.append(A)
        if self.rowCheck(M, stk) and self.colCheck(M, stk) == True:
            return stk[0]
        else:
            return -1
s = Solution()
print(s.celebrity([[0, 1, 0],
         [0, 0, 0],
         [0 ,1, 0]],3))