class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n=max(nums)
        nums.sort()
        c=nums[0]
        arr=[]
        while c<n:
            if c not in nums:
                arr.append(c)
            c+=1
        return arr