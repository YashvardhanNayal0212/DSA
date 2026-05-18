class Solution:
    def minElement(self, nums: List[int]) -> int:
        m=float("inf")
        for i in range (len(nums)):
            sum=0
            while nums[i]>0:
                n=nums[i]%10
                sum+=n
                nums[i]//=10
            m=min(sum,m)
        return m