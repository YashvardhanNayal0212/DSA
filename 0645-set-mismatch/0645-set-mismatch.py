class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = []
        s = set(nums)

        for i in nums:
            if nums.count(i) == 2:
                arr.append(i)
                break

        for i in range(1, len(nums) + 1):
            if i not in s:
                arr.append(i)
                break

        return arr