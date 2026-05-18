class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        l=0
        count=0
        r=len(nums)-1
        leftsum=0
        rightsum=sum(nums)
        for i in range (r):
            leftsum+=nums[i]
            rightsum-=nums[i]
            if (leftsum-rightsum)%2==0:
                count+=1
        return count