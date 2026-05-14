class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range (len(nums)):
            temp=[]
            n=nums[i]
            while n>0:
                temp.append(n%10)
                n//=10
            arr.extend(temp[::-1])
        return arr