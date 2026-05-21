class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        pos,neg=0,1
        for i in range (len(nums)):
            if nums[i]>0:
                arr[pos]=nums[i]
                pos+=2
            else:
                arr[neg]=nums[i]
                neg+=2
        return arr
                