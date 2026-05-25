class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        c=0
        for i in nums:
            while i!=0:
                n=i%10
                if n==digit:
                    c+=1
                i//=10
        return c