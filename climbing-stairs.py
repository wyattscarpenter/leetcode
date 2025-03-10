class Solution:
    def climbStairs1(self, n: int) -> int:
        """mfw I notice this is just the fibonacci numbers"""
        f=self.climbStairs
        if n==0: return 1
        if n==1: return 1
        return f(n-1)+f(n-2)
    def climbStairs(self, n: int) -> int:
        """mfw I notice the time limit is exceeded by the naive solution"""
        acc, prev = 1, 0
        while n:
            acc, prev, n = prev+acc, acc, n-1 #code written this way just to look funny 😛
        return acc
