class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left=1
        right=x//2
        while left<=right:
            n=(right+left)//2
            if n*n==x:
                return n
            elif n*n<x:
                left=n+1
            else:
                right=n-1
        return right


            