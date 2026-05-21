class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        m=0
        while l<=r:
            s=nums[l]+nums[r]
            m=max(m,s)
            l+=1
            r-=1
        return m