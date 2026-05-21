class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        while l<r:
            s=nums[r]+nums[l]
            if s==0:
                return nums[r]
            elif s>0:
                r-=1
            else:
                l+=1
        return -1