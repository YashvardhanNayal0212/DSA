class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        arr = []

        for i in range(min(nums), max(nums)):
            if i not in s:
                arr.append(i)

        return arr