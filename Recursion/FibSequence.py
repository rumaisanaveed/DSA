class Solution:
    def fib(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)
s = Solution()
print(s.fib(2))