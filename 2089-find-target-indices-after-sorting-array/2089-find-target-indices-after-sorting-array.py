class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new=sorted(nums)
        a=[]
        for i in range(len(new)):
            if new[i]==target:
                a.append(i)
        return a