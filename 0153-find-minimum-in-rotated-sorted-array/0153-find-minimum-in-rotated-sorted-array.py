class Solution:
    def findMin(self, nums: List[int]) -> int:
        m=float("inf")
        for i in nums:
            m=min(m,i)
        return m