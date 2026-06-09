class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n=max(nums)-min(nums)
        return n*k