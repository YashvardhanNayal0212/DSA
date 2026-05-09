class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        prod=nums[0]*nums[1]
        diff=nums[-1]*nums[-2]
        return abs(prod-diff)