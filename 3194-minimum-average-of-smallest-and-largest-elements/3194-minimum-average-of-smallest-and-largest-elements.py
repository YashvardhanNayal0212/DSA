class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l,r=0,len(nums)-1
        m=float("inf")
        while l<=r:
            avg=(nums[l]+nums[r])/2
            l+=1
            r-=1
            m=min(m,avg)
        return m