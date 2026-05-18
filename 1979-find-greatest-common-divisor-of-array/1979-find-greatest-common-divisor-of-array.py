class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m=float("inf")
        n=0
        ans=1

        for i in range(len(nums)):
            m=min(nums[i],m)
            n=max(nums[i],n)
        
        for i in range(1,m+1):
            if m%i==0 and n%i==0:
                ans=i
        return ans