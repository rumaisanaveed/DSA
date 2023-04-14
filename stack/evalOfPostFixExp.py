from queue import LifoQueue
class Solution():
    def evaluatePostfix(self,exp):
        stack = LifoQueue()
        for i in range(len(exp)):
            if exp[i].isdigit():
                stack.put(exp[i])
            else:
                operand1 = stack.get()
                operand2 = stack.get()
                result = str(eval(operand2 + exp[i] + operand1))
                stack.put(result)
        return stack.get()
s = Solution()
print(s.evaluatePostfix("231*+9-"))