class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        count=0
        for i in nums:
            n=m-i
            count+=n
        return count