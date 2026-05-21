class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr=[]
        temp=[]
        count=0
        for i in nums:
            if i<pivot:
                arr.append(i)
            elif i>pivot:
                temp.append(i)
            else:
                count+=1
        return arr+[pivot]*count+temp