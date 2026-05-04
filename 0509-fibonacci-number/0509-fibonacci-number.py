class Solution:
    def fib(self, n: int) -> int:
        a=fib=0
        b=1
        if n<2:
            return n

        for i in range (1,n):
            fib=a+b
            a=b
            b=fib
        return fib
