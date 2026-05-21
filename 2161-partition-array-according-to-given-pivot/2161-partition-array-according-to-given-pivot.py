class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr=[]
        temp=[]
        count=0
        for i in range(len(nums)):
            if nums[i]<pivot:
                arr.append(nums[i])
            elif nums[i]>pivot:
                temp.append(nums[i])
            else:
                count+=1
        return arr+[pivot]*count+temp